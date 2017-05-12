#encoding:utf-8
def test31():
	days = [('M',1),('TU',2),('W',3),('TH',4),('F',5),('SA',6),('SU',7)]
	fristCap = 'M'
	secondCap = 'U'
	for inputStr,intDay in days:
		l = list(inputStr)
		if len(l) == 1 and inputStr == fristCap:
			print intDay
			return
		if len(l) == 2 and fristCap == l[0] and secondCap == l[1]:
			print intDay
			return

def test32():
	a = ['one','two','three']
	print [i for i in a[::-1]]

def test33():
	a = [1,3,5,7,9]
	print ",".join([str(i) for i in a])

def test35():
	class bcolors:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
	print bcolors.WARNING + "警告颜色"+bcolors.ENDC

import math	
import random
def test36():
	for i in xrange(2,100):
		flag = True
		for j in xrange(2,int(math.sqrt(i)+1)):
			if i % j == 0:
				flag = False
				break
		if flag:
			print i

def test37():
	N = 10
	l = []
	for i in xrange(N):
		l.append(int(random.uniform(10,100)))
	for i in xrange(N-1):
		minV = i
		for j in xrange(i+1,N):
			if l[minV] > l[j]:
				minV = j
		l[i],l[minV] = l[minV],l[i]
	print 'after sorted'
	for i in xrange(N):
		print l[i]

def test38():
	a = [[1,2,3],[4,5,6],[7,8,9]]
	b = [a[i][j] for i in range(3) for j in range(3) if i == j]
	print sum(b)

test38()



