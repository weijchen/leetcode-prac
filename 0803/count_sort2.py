# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: count sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/countingsort2/problem
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

for i in range(len(numlis)):
	if int(numlis[i]) > 0:
		for j in range(int(numlis[i])):
			print(i, end=' ')