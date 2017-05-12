import os
onlyNumbers = []
onlyWorlds = []
for i in xrange(26):
	onlyWorlds.append(chr(97+i))
for i in xrange(26):
	onlyWorlds.append(chr(65+i))
for i in xrange(9):
	onlyNumbers.append(chr(ord('0')+i))

onlyChars = list('!@#$%^&*()_+|[]{}<>,.~`"\':;?/')
numberAndWorlds = onlyNumbers + onlyWorlds
allChars = numberAndWorlds + onlyChars

def testBit(bit,char_list):
	


min_bit = 4
max_bit = 10

	


