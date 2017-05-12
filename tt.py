# import json
# class Person:
# 	def __init__(self, dict_v):
# 		self.pid = int(dict_v['pid'])
# 		self.nickname = dict_v['nickname']
# 		self.age = int(dict_v['age'])
# 	def __str__(self):
# 		return "pid:%d nickname:%s age:%d" % (self.pid,self.nickname,self.age)

# jsonStr ='{"total":2,"person":[{"pid": "1","nickname": "zhangsan","age": "22"},{"pid": "2","nickname": "lisi","age": "27"}]}'
# jsObj = json.loads(jsonStr)
# total = jsObj['total']
# pl = jsObj['person']
# personlist = []
# for pDict in pl:
# 	personlist.append(Person(pDict))

# for p in  personlist:
# 	print p

def findOther(ls,count):
	if count == 1:
		return ls[0]
	else：
		return findOther(ls[1:], count-1)