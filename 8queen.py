def conflict(state,nextX):
	nextY = len(state)
	for i in xrange(nextY):
		if abs(state[i]-nextX) in (0,nextY-i):
		   return True
	return False

def queens(num=8,state=()):
	for pos in xrange(num): #every line
		if not conflict(state,pos):  
			if len(state) == num-1: #if not conflict and state's length == num-1 ,print pos
				yield (pos,)
			else:
				for result in queens(num,state+(pos,)): #else print all
					yield (pos,)+result

print len(list(queens(8)))
for solution in queens(8):
	print solution