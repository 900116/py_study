#encoding:utf-8
import urllib
import urllib2
import re
import net_study

#糗事百科爬虫类
class QSBK:
	def __init__(self):
	 	self.pageIndex = 1
	 	self.url_base = 'http://www.qiushibaike.com/hot/page/'
	 	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	 	self.headers = { 'User-Agent' : user_agent }
	 	self.stories = []
	#获取某页面代码
	def getPage(self,pageIndex):
	 	try:
	 		url = self.url_base + str(pageIndex)
	 		content = net_study.get(url,headers=self.headers)
	 		return content
	 	except urllib2.URLError,e:
	 		if hasattr(e, "reason"):
	 			print u"连接失败",e.reason
	 			return None

	def getPageItems(self,pageIndex):
	 	content = self.getPage(pageIndex)
	 	if not content:
	 		print "页面加载失败"
	 		return None
	 	pattern = re.compile('<div class="author clearfix">.*?<a.*?<a.*?<h2>(.*?)</h2>.*?<div.*?<a.*?<div class="content">.*?<span>(.*?)</span>.*?number">(.*?)</i>.*?number">(.*?)</i>',re.S)
	 	items = re.findall(pattern, content)
	 	pageStories = []
	 	for author,content,haoxiao,pinglun in items:
	 		content = content.replace('<br>','\n')
	 		content = content.replace('<br/>','\n')
			pageStories.append((author,content,haoxiao,pinglun))	 		
		return pageStories

	def loadPage(self):
		page = self.pageIndex
		print "正在加载第%d页面..."%page
		pageStories = self.getPageItems(self.pageIndex)
		if pageStories:
			self.stories.append(pageStories)
			self.pageIndex += 1
			return True
		else:
			print "第%d页加载失败"%page
			return False


	def start(self):
		key = raw_input("正在读取糗事百科,按回车确认，任意键退出:")
		break_flag = False
		if key != '':
			break_flag = True
		currPage = 0

		while not break_flag:
			if currPage > len(self.stories)-1:
				if not self.loadPage():
					currPage -= 1
					continue
			tieziList = self.stories[currPage]
			for author,content,haoxiao,pinglun in tieziList:
				print "*"*100
				print "\n"
				print "作者: " + author + "\n"
				print "内容：\n" + content
				print "\n好笑: " + haoxiao
				print "\n评论: " + pinglun
				print "\n"

			sub_break_flag = False
			while not sub_break_flag:
				print "当前第%d页" % (currPage+1)
				key = raw_input("按回车键获取下一页，按q键获取上一页，按其他键退出:")
				if key == '':
					currPage+=1
					sub_break_flag = True
				elif key == 'q':
					if currPage < 1:
						print "当前已经是第一页"
					else:
						currPage-=1
						sub_break_flag = True
				else:
					sub_break_flag = True
					break_flag = True
		print "程序已经退出"

spider = QSBK()
spider.start()