import math
import time
def test1():
	print [(i,j,k) for i in range(1,5) for j in range(1,5) for k in range(1,5) if i!=j and j!=k and i!=k]

def test2():
	i = 420000
	arr = [(1000000,0.01),(600000,0.015),(400000,0.03),(200000,0.05),(100000,0.075),(0,0.1)]
	r = 0
	for minV,rate in arr:
		if i > minV:
			r += (i - minV)* rate
			i = minV
	print r

def test3():
	print [i for i in xrange(1,10000) if int(math.sqrt(i+100)) == math.sqrt(i+100) and int(math.sqrt(i+268)) == math.sqrt(i+268)]

def test4():
	year = 2015
	month = 6
	day = 7
	days = [31,28,31,30,31,30,31,31,30,31,30,31]
	if year % 4 == 0 and year % 100 !=0:
		days[1]+=1
	print sum(days[:month-1])+day

def test5():
	l = []
	x = 8
	l.append(x)
	y = 5
	l.append(y)
	z = 6
	l.append(z)
	l.sort()
	print l

def Fib(n):
	if n == 1 or n == 2:
		return 1
	return Fib(n-1) + Fib(n-2) 

def Fib_G(n):
 	for x in xrange(1,n+1):
		if x == 1:
		   a = x 
		   yield a
		elif x == 2:
		   b = 1
		   yield b
		elif x%2 == 1:
		   a += b
		   yield a
		else: 
		    b += a
		    yield b

def test6():
	print list(Fib_G(10))

def test7():
	a = [1,2,3]
	b = a[:]
	print b

def test8():
	for i in xrange(1,10):
		for j in xrange(1,i+1):
			print "%d*%d = %d"%(i,j,i*j),
		print "\n"

def test9():
	print 3
	time.sleep(1)
	print 4

def test10():
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def test11():
	print 2*Fib(10)

def test12():
	total = 0
	for i in xrange(101,201):
		isSu = True
		for j in xrange(2,int(math.sqrt(i))+1):
			if i % j == 0:
				isSu = False
				break
		if isSu:
			total+=1
			print i
	print "this total is %d" % total

def test13():
	print [x for x in xrange(100,1000) if (int(x/100)**3 + ((x/10)%10)**3 + (x%10)**3) == x]

def test14():
	i = 120
	l = []
	while i != 1:
		for x in xrange(2,i+1):
			if i % x == 0:
				i /= x
				l.append(x)
				break
	l.sort()
	print "*".join([str(j) for j in l])	

def test15():
	score = 89
	if score > 100 or score < 0:
		print "error"
	elif score < 60:
		print "C"
	elif score < 90:
		print "B"
	else:
		print "A"

import datetime
def test16():
	print datetime.date.today().strftime("%d/%m/%Y")
	date_t = datetime.date(1978, 12, 25)
	print date_t.strftime("%Y-%m-%d")
	date_t = date_t + datetime.timedelta(days=1)
	print date_t.strftime("%Y-%m-%d")
	date_t = date_t.replace(year=date_t.year+1)
	print date_t.strftime("%Y-%m-%d")

import string
import re
def test17():
	text = "awepriewejoiwE1231231 dFeoi vw q qwqjwowje fwejio 123 wfjoij .323 e3[]\=-09"
	letters = len(re.compile("[a-zA-Z]").findall(text))
	spaces = text.count(' ')
	digits = len(re.compile("[0-9]").findall(text))
	others = len(text)-spaces-digits-letters
	print letters,spaces,digits,others

def test18():
	a = 4
	n = 2
	total = 0
	for i in xrange(1,n+1):
		l = []
		for j in xrange(1,i+1):
			l.append(str(a))
		total+=int("".join(l))
	print total

def inzs(i):
	for x in xrange(1,i):
		if i % x == 0:
			yield x

def test19():
	print [x for x in xrange(2,1000) if sum(inzs(x)) == x]

def test20():
    Sn = 100.0
    for i in xrange(1,11):
    	Sn /= 2
    print Sn 

def test21():
 	total = 1
 	for x in xrange(1,5):
 		total = (total+1)*2
 	print total

def test22():
	yi =  ['x','y','z']
	for a in yi:
		for b in yi:
			if a!=b:
				for c in yi:
					if a!=c and b!=c:
						if a!='x' and c!='x' and c!='z':
							print [("a",a),("b",b),("c",c)]

def test23():
	total_stars = 9
	total_lines = total_stars*2 + 1
	for x in xrange(1,total_lines+1,2):
		stars = (x if x<=total_stars else total_stars-(x-total_stars))
		spaces = (total_stars-stars)/2
		print " "*spaces + "*"*stars + " "*spaces

def test24():
	fenzi = list(Fib_G(22))[2:]
	fenmu = list(Fib_G(21))[1:]
	print sum([float(x)/float(y) for x,y in zip(fenzi,fenmu)])

def test25():
	print sum([math.factorial(x) for x in xrange(1,21)])

def my_factorial(x):
	if x == 1:
		return x
	return x*my_factorial(x-1)
def test26():
	print my_factorial(5)

def my_test27_output(l):
	if len(l) == 1:
		print l[0]
	else:
		print l[len(l)-1]
		l = l[:len(l)-1]
		my_test27_output(l)

def test27():
	l = ['a','b','c','d','e']
	my_test27_output(l)

def test28():
	all_people = 5
	begin_age = 10
	for i in xrange(2,all_people+1):
		begin_age+=2
	print begin_age

def test29():
	x = 12356
	l = list(str(x))
	print len(l)
	l.reverse()
	print l

def test30():
	number = 12321
	x = str(number)
	flag = True
	for i in xrange(len(x)/2):
		if x[i] != x[-i-1]:
			flag = False
	print flag