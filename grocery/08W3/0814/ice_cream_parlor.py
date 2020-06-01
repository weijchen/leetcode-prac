# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: count sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/icecream-parlor/problem
''' 
# --------------------------------------------------- libs import
import sys

t = 2
m_1 = 4
n_1 = 5
c_1 = [1, 4, 5, 3, 2]
m_2 = 4
n_2 = 4
c_2 = [2, 2, 4, 3]

answerlis = []

t = int(input())
for i in range(t):
	m = int(input())
	n = int(input())
	li = [int(i) for i in input().strip().split()]
	a_flavor = 0
	b_flavor = 0
	flavor_set = []
	for i in range(len(li)):
		a_flavor = li[i]
		for j in range(i+1, len(li)):
			b_flavor = li[j]
			if a_flavor + b_flavor == m:
				flavor_set.append((i+1, j+1))
	answerlis.append((flavor_set[0][0], flavor_set[0][1]))
for i in range(len(answerlis)):
	print(answerlis[i][0], answerlis[i][1])