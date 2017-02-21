#encoding:utf-8
import urllib
import urllib2
import re
import net_study
from worm_base import WormBase

#糗事百科爬虫类
class QSBK(WormBase):
	def __init__(self):
	 	self.pageIndex = 0
	 	self.url_base = 'http://www.qiushibaike.com/hot/page/'
	 	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	 	self.headers = { 'User-Agent' : user_agent }
	 	self.stories = []
	#获取某页面代码
	def getPage(self,pageIndex):
	 	try:
	 		url = self.url_base + str(pageIndex+1)
	 		content = net_study.get(url,headers=self.headers)
	 		return content
	 	except urllib2.URLError,e:
	 		if hasattr(e, "reason"):
	 			print u"连接失败",e.reason
	 			return None

	def getPageItems(self):
	 	content = self.getPage(self.pageIndex)
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

	def curr_page_content(self):
		if self.pageIndex > len(self.stories) - 1:
			self.stories.append(self.getPageItems())
		tz_list = self.stories[self.pageIndex]
		show_items = []
		for author,content,haoxiao,pinglun in tz_list:
			s = "\n"
			s+=  "\n"
			s+=  "作者: " + author + "\n"
			s+=  "内容：\n" + content
			s+=  "\n好笑: " + haoxiao
			s+=  "\n评论: " + pinglun
			s+=  "\n"
			show_items.append(s)
		return show_items