#encoding=utf-8
class WormBase():
	def __init__(self):
		self.pageIndex = 0
		self.totalPage = 0
		self.title = ""
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

	def start(self):
		input_v = raw_input("正在扫描%s，按回车键继续，其他键退出:" % self.title)
		if input_v != '':
			print "程序已退出"
			return
		ls = self.curr_page_content()
		show_flag = True
		while True:
			if show_flag:
				for line in ls:
					print line
			input_v = raw_input("当前第%d页，按回车键获取下一页，按q键获取上一页，其他键退出:" % (self.pageIndex+1))
			show_flag = True
			if input_v == '':
				temp = self.next_page()
				if temp != None:
					ls = temp
				else:show_flag = False
			elif input_v.lower() == 'q':
				temp = self.last_page()
				if temp != None:
					ls = temp
				else:show_flag = False
			else:
				print "程序已退出"
				return
