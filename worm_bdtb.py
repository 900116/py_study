#encoding=utf-8
import urllib
import urllib2
import re
import net_study

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
class BDTB(object):
	def __init__(self, baseUrl,onlyLZ=0):
		self.baseUrl = "http://tieba.baidu.com/p/" + baseUrl
		self.onlyLZ = '?see_lz='+str(onlyLZ)
		self.title = None
		self.totalPage = 0
		self.currPage = 1
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
			if self.currPage > len(self.pages):
				self.pages.append(result_new)	
			else:
				self.pages[self.currPage-1] = result_new

	def display(self):
		page_content = self.pages[self.currPage-1]
		i = 0
		for author,content,time in page_content:
			if i == 0 and self.currPage == 1:
				self.lz = author
			if author == self.lz:
				print "【楼主】"
			print "作者: " + author
			print "内容: \n" + content
			print "时间: " + time
			print '-'*100+'\n'
			i+=1
		print "^"*30+"【" + self.title + "】"+"^"*30
		print "第%d页/共%d页" % (self.currPage,self.totalPage)

	def nextPage(self):
		if self.currPage == self.totalPage:
			print "没有更多了"
		else:
			self.currPage+=1
			self.getPage()

	def lastPage(self):
		if self.currPage == 1:
			print "已经是第一页"
		else:
			self.currPage-=1
			self.getPage()

	def getPage(self):
		if self.pages > len(self.pages) or self.lastOnlyLZ != self.onlyLZ:
			params = {'pn':str(self.currPage),'see_lz':self.onlyLZ}
			self.content = net_study.get(self.baseUrl,params=params)
			self.find_title()	
			self.find_totalpage()
			self.find_content()
			self.lastOnlyLZ == self.onlyLZ
		self.display()


if __name__ == "__main__":
		key = raw_input("欢迎使用百度贴吧阅读器，请输入要浏览的帖子编号,输入0退出:")
		BreakFlag = False
		if key == "0":
			BreakFlag = True
		bdtb = BDTB(key)
		bdtb.getPage()
		while not BreakFlag:
			key = raw_input("按回车键获取下一页内容，按q键获取上一页内容\n按z键切换到只看楼主,按c键回到正常模式，按其他键退出:")
			if key == '':
				bdtb.nextPage()
			elif key == 'q':
				bdtb.lastPage()
			elif key == 'z':
				bdtb.onlyLZ = 1
				bdtb.getPage()
			elif key == 'c':
				bdtb.onlyLZ = 0
				bdtb.getPage()
			else:
				break
		print "程序已经退出"
