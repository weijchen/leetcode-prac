#!/bin/python3

# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Week of code 34, Created Jul. 2017
Ver: 1.0 (finish)
Link: 
''' 
# --------------------------------------------------- libs import
import sys
# --------------------------------------------------- solution
def onceInATram(x):
	x += 1
	lis = []
	for i in range(0, 6):
		lis.append(str(x)[i])

	first_half = int(lis[0]) + int(lis[1]) + int(lis[2])
	second_half = int(lis[3]) + int(lis[4]) + int(lis[5])

	if first_half == second_half:
		print(x)
	else:
		onceInATram(x)


# x = 555555
x = int(input().strip())
result = onceInATram(x)
