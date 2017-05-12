def num2char(x):
	return chr(ord('0')+x)

def num2str(value):
	l = []
	l.append(value%10)
	while value > 10:
		value = value/10
		l.append(value % 10)
	l.reverse()
	result = ''
	for i in l:
		result += num2char(i)
	return result

print num2str(123456)