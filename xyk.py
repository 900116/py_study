#encoding=utf-8
import gh_file

class YHK:
	yh = ''
	edu = 0
	return_day = 0
	sy_edu = 0
	number = 0
	d_time = 0

	def __init__(self,tp):
		yh,number,return_day,edu,sy_edu,d_time = tp
		self.yh = yh
		self.number = number
		self.edu = edu
		self.return_day = return_day
		self.sy_edu = sy_edu
		self.d_time = d_time

	def get_max_shua(self):
		return self.edu * 0.2

	def shua_total_everyday(self):
		return self.edu / self.d_time

	def can_shua(self):
		return edu > 0

	def get_all_shua(self):
		list_shua = []
		sy = self.shua_total_everyday()
		while sy:
			shua = float("%.1f" % random.uniform(105.3, self.get_max_shua()))
			if sy < shua:
				shua = float("%.1f" % sy) 
				list_shua.append(shua)
				break
			sy -= shua
			list_shua.append(shua)
		return list_shua



def find_should_huan_item(day,item_list):
	j = 0
	for item in item_list:
		if day == item.return_day-1:
			return (item,True,j)
		if day < item.return_day-1:
			return (item,False,j)
		j+=1
	return (item_list[0],False,j)

def find_shua_item(day,item_list):
	j = 0
	for item in item_list:
		if day < item.return_day-1:
			return item,j
		j+=1
	return None,0

def total_edu(item_list):
	total = 0
	for item in item_list:
		total += item.edu
	return total

tuple_list = []
tuple_list.append(YHK(('北京银行','1234',13,12000,0,0)))
tuple_list.append(YHK(('中国银行','2351',16,12000,0,0)))
tuple_list.append(YHK(('工商银行','5643',18,30000,0,0)))
tuple_list.append(YHK(('招商银行','1237',21,24000,0,0)))
tuple_list.append(YHK(('交通银行','2352',25,50000,50000,0)))

tuple_time_list = sorted(tuple_list,key=lambda x:x.return_day)
lastday = 0
count = len(tuple_time_list)-1
for i in range(count,-1,-1):
	item = tuple_time_list[i]
	if i == count:
		item.d_time = tuple_time_list[0].return_day
	else:
		item.d_time = lastday - item.return_day
	lastday = item.return_day
	i+=1
tuple_edu_list = sorted(tuple_list,key=lambda x:x.edu)
total = total_edu(tuple_edu_list) - tuple_edu_list[len(tuple_edu_list)-1].edu

import random
print "最大能透支金额为：%s" % total
for i in range(1,32):
	item,hkr,item_idx = find_should_huan_item(i, tuple_time_list)
	shua_item,shua_idx = find_shua_item(i, tuple_time_list)
	print "----%d-----" % i
	if shua_item: 
		shua_list = shua_item.get_all_shua()
		print "可以刷卡 %s:%s 共刷%d笔,每笔金额:%s" %(shua_item.yh,shua_item.number,len(shua_list),shua_list)
	if hkr:
		print "今天需要还 %s:%s 金额为:%s" % (item.yh,item.number,item.edu) 
		item.sy_edu = item.edu
	else: 
		print "最近待还卡为 %s:%s" % (item.yh,item.number)
