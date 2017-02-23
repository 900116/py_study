#encoding=utf-8
import os
import urllib2
import threading
import Queue
import net_study

q = Queue.Queue()
threading_num = 5

domain_name = "http://www.zasv.com"
Baidu_spider = "Mozilla/5.0 (compatible; Baiduspider/2.0; + http://www.baidu.com/search/spider.html)"
execute_list = ['.jpg','.gif','.css','.png','.js','.scss']

f = open("dict","r")
lines = f.readlines()
f.close()

for line in lines:
	line = line.rstrip()
	if os.path.splitext(line)[1] not in execute_list:
		q.put(line)

def crawler():
	while not q.empty():
		path = q.get()
		url = "%s%s" % (domain_name,path)
		headers = ['User-Agent'] = Baidu_spider
		content = net_study.get(url,headers=headers)

for i in range(threading_num):

