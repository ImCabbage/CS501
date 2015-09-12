#!/usr/bin/python

# This is a simple program on calculating alphabetic character.
# It is No.3 problem in HW 1

import sys
L = list(sys.argv[1])                   # transfer to string to list
Result = [0]*26

for x in L:                        # classification
	if str.isalpha(x) == 1:
		y = str.lower(x)
		y = ord(y)-97;
		Result[y] = Result[y]+1;

for i in range(26):                # output the result
	if Result[i] != 0:
		print (chr(i+97),': ',Result[i])

		