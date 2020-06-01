# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: count sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/countingsort4
''' 
# --------------------------------------------------- libs import
import sys

# n = input()
# ar = [int(i) for i in input().strip().split()]
n = 10
ar = [-20, -3916237, -357920, -3620601, 7374819 ,-7330761, 30 ,6246457, -6461594, 266854]
ar.sort()
diff = abs(ar[0] - ar[1])
answerlis = []
for i in range(1, len(ar)-1):
	num_1 = ar[i]
	num_2 = ar[i+1]
	test = abs(num_1 - num_2)
	if test < diff:
		answerlis = []
		answerlis.append(num_1)
		answerlis.append(num_2)
		diff = abs(num_1 - num_2)
	elif test == diff:
		answerlis.append(num_1)
		answerlis.append(num_2)
print(' '.join(str(x) for x in answerlis))