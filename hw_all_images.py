#encoding=utf-8
from urllib import urlretrieve
from urllib import urlopen 
import re
import os.path
import time
import socket

def read(url):
	webpage = urlopen(url)
	text = webpage.read()
	return text

#查找所有图片模块
def find_all_pics_models(url,host):
	content = read(url)
	models =re.findall('(?m)<ul class="menu mt5">.*?</ul>', content,re.S)
	for model in models:
		if model.find('图片')!=-1:
			pic_model = model
			break
	lis = re.findall('(?m)<li><a href="(.*?)">(.*?)</a></li>', pic_model,re.S)
	result = []
	for url,model_name in lis:
		result.append((model_name,host+url))
	return result

def find_all_imgs(text):
 	result = re.findall(r'src *= *"(.+?(.jpg|.png|.gif))"',text)
 	imglist = [i for i,j in result]
 	return imglist

#查找当前模块下第一个帖子的地址
def find_model_first_url(model_url):
	text = read(model_url)
	tl = re.findall('(?m)<li><a href="(.*?)" .*?><span>\d{4}-\d{2}-\d{2}</span>(.*?)</a></li>', text,re.S)
	return tl[1]

#查找下一个帖子
def find_next_one(url):
	content = read(url)
	tl = re.findall("(?m)上一篇:<a href='(.*?)'>(.*?)</a></span> <span>下一篇:", content,re.S)
	return tl

#抓取当前页面的所有图片，并递归下一篇
def find_all_images(url,host,title,parentPath):
	page_Path = os.path.join(parentPath,title)
	if not os.path.exists(page_Path):
		os.mkdir(page_Path)
	page_url = host+url
	content = read(page_url)
	imglist = find_all_imgs(content)
	print "开始下载:"+title
	for imgurl in imglist:
		file_name = imgurl.split('/')[-1]
		image_file_path = os.path.join(page_Path,file_name)
		if not os.path.exists(image_file_path):
			socket.setdefaulttimeout(10)
			try:
				urlretrieve(imgurl,image_file_path)
			except Exception,e:
				continue
			time.sleep(0.5)
		print imgurl + "----下载完成"
	tl = find_next_one(page_url)
	print title+"----下载完成"
	if len(tl) > 0:
		nexturl,nexttitle = tl[0]
		find_all_images(nexturl, host, nexttitle, parentPath)

if __name__ == "__main__":
	savePath = "ht"
	if not os.path.exists(savePath):
		os.mkdir(savePath)
	host = "http://www.yiren22.com"
	model_url = "/se/yazhousetu/564305.html"
	firstpage = host+model_url
	pic_models = find_all_pics_models(firstpage,host)
	print "模块扫描完毕"
	for modelName,url in pic_models:
		print "开始下载:"+modelName
		modelPath = os.path.join(savePath,modelName)
		if not os.path.exists(modelPath):
			os.mkdir(modelPath)
		model_frist_url,title = find_model_first_url(url)
		find_all_images(model_frist_url,host,title,modelPath)
		print modelName + "----下载完成"
