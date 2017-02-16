#encoding=utf-8
from urllib import urlretrieve
from urllib import urlopen 
import re
import os.path
import time

def read(url):
	webpage = urlopen(url)
	text = webpage.read()
	return text

#查找所有图片模块
def find_all_novels_models(url,host):
	content = read(url)
	models =re.findall('(?m)<ul class="menu mt5">.*?</ul>', content,re.S)
	for model in models:
		if model.find('小说')!=-1:
			novel_model = model
			break
	lis = re.findall('(?m)<li><a href="(.*?)">(.*?)</a></li>', novel_model,re.S)
	result = []
	for url,model_name in lis:
		result.append((model_name,host+url))
	return result

#查找当前模块下第一个帖子的地址
def find_model_first_url(model_url):
	text = read(model_url)
	tl = re.findall('(?m)<li><a href="(.*?)" .*?><span>\d{4}-\d{2}-\d{2}</span>(.*?)</a></li>', text,re.S)
	return tl[1]

#查找小说内容
def find_novel_content(content):
	tl = re.findall('(?m)<tbody><tr><td>(.*)</td></tr></tbody>', content,re.S)
	return tl[0]

#查找下一个帖子
def find_next_one(url):
	content = read(url)
	tl = re.findall("(?m)上一篇:<a href='(.*?)'>(.*?)</a></span> <span>下一篇:", content,re.S)
	return tl

#抓取当前页面的所有小说，并递归下一篇
def find_all_novels(url,host,title,parentPath):
	page_Path = os.path.join(parentPath,title+".txt")
	page_url = host+url
	print "开始下载:"+title
	content = read(page_url)
	content = find_novel_content(content)
	content = content.replace('<br />','\n')
	if not os.path.exists(page_Path):
		f = open(page_Path,'w')
		f.write(content)
		f.close()
	print title+"----下载完成"
	tl = find_next_one(page_url)
	if len(tl) > 0:
		nexturl,nexttitle = tl[0]
		find_all_novels(nexturl, host, nexttitle, parentPath)

if __name__ == "__main__":
	savePath = os.path.expanduser("~/Desktop/ht/")
	host = "http://www.yiren22.com"
	model_url = "/se/yazhousetu/564305.html"
	firstpage = host+model_url
	novel_models = find_all_novels_models(firstpage,host)

	print "模块扫描完毕"
	for modelName,url in novel_models:
		print "开始下载:"+modelName
		modelPath = os.path.join(savePath,modelName)
		if not os.path.exists(modelPath):
			os.mkdir(modelPath) 
		model_frist_url,title = find_model_first_url(url)
		find_all_novels(model_frist_url,host,title,modelPath)
		print modelName + "----下载完成"