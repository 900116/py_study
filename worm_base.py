#encoding=utf-8
class WormBase():
	def __init__(self):
		self.pageIndex = 0
		self.totalPage = 0
	def curr_page_content(self):
		return None

	def next_page(self):
		if self.pageIndex+1 > self.totalPage and self.totalPage!=0:
			print "已经是最后一页"
			return None
		self.pageIndex+=1
		return self.curr_page_content()

	def last_page(self):
		if self.pageIndex < 1:
			print "当前已经是第一页"
			return None
		else:
			self.pageIndex -=1
		return self.curr_page_content()
