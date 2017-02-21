#encoding=utf-8
from worm_qxbk import *
from worm_bdtb import *
from Tkinter import *
worm = QSBK()
worm = BDTB("657940638")
l = worm.curr_page_content()
root=Tk()   #主窗口
root.geometry("600x400")
lb = Listbox(root)

def refresh_lb(l):
	if l != None:
		lb.delete(0,END)
		for x in l:
			lb.insert(END,x)

def last_action():
	l = worm.last_page()
	refresh_lb(l)

def next_action():
	l = worm.next_page()
	refresh_lb(l)

refresh_lb(l)
lb.pack(fill=BOTH,expand=1)

last = Button(root,text='上一页',command=last_action,activeforeground='white',
activebackground='red')
last.pack(side=LEFT)

next = Button(root,text='下一页',command=next_action,activeforeground='white',
activebackground='red')
next.pack(side=LEFT)

quit = Button(root,text='关闭程序',command=root.quit,activeforeground='white',
activebackground='red')
quit.pack(side=LEFT)
mainloop()
