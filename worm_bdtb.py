#encoding=utf-8
import urllib
import urllib2
import re
import net_study
from worm_base import WormBase

#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    replaceSpace = re.compile('&nbsp;')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        x = re.sub(self.replaceSpace, " ", x)
        #strip()将前后多余内容删除
        return x.strip()


#百度贴吧爬虫类
class BDTB(WormBase):
	def __init__(self, baseUrl,onlyLZ=0):
		WormBase.__init__(self)
		self.baseUrl = "http://tieba.baidu.com/p/" + baseUrl
		self.onlyLZ = '?see_lz='+str(onlyLZ)
		self.title = None
		self.totalPage = 0
		self.tool = Tool()
		self.pages = []
		self.lastOnlyLZ = onlyLZ

	#获取标题
	def find_title(self):
		if self.title != None:
			return
		pattern = re.compile('<h\d class="core_title_txt.*?>(.*?)</h\d>',re.S)
		result = re.findall(pattern, self.content)
		if result:
			self.title = result[0]
		else:
			self.title = None

	#获取总页数
	def find_totalpage(self):
		if self.totalPage != 0:
			return
		pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span class="red">(.*?)</span>',re.S)
		result = re.findall(pattern, self.content)
		if result:
			self.totalPage = int(result[0])
		else:
			self.totalPage = 0

	#获取内容
	def find_content(self):
		pattern = re.compile('<li class="d_name".*?<a.*?>(.*?)</a>.*?<div id="post_content_.*?>(.*?)</div>.*?(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).*?<div class="clear">',re.S)
		result = re.findall(pattern, self.content)
		if result:
			result_new = []
			for author,content,time in result:
				content = self.tool.replace(content)
				result_new.append((author,content,time))
			if self.pageIndex > len(self.pages)-1:
				self.pages.append(result_new)	
			else:
				self.pages[self.pageIndex] = result_new

	def curr_page_content(self):
		self.getPage()
		tz_list = self.pages[self.pageIndex]
		show_items = []
		i = 0
		for author,content,time in tz_list:
			s = ""
			if i == 0 and self.pageIndex == 0:
				self.lz = author
			if author == self.lz:
				s+= "【楼主】"
			s+=  "作者: " + author
			s+=  "内容: \n" + content
			s+=  "时间: " + time
			i+=1
			show_items.append(s)
		return show_items

	def getPage(self):
		if self.pageIndex > len(self.pages)-1 or self.lastOnlyLZ != self.onlyLZ:
			params = {'pn':str(self.pageIndex+1),'see_lz':self.onlyLZ}
			self.content = net_study.get(self.baseUrl,params=params)
			self.find_title()	
			self.find_totalpage()
			self.find_content()
			self.lastOnlyLZ == self.onlyLZ