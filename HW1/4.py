#! /usr/bin python
# This is a interesting game on simple calculating
# It is No.4 problem in HW 1

import random
try:
	while (1):
		s = 1;
		a = random.randrange(1,10)
		b = random.randrange(1,10)
		c = a + b
		print a,' + ',b,' = ?'
		while (s):
			answer = input()
			answer = int(answer)
			if answer == c:
				s = 0
				print ('Correct.')
			else:
				print ('Incorrect; try again')
except EOFError:
	print ('Good bye.')


