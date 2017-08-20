# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: count sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/countingsort1/problem
''' 
# --------------------------------------------------- libs import
import sys

n = input()
ar = [int(i) for i in input().strip().split()]

numlis = []
for i in range(0, 100):
	count = 0
	for j in ar:
		if i == j:
			count += 1
	numlis.append(str(count))
print(' '.join(numlis))