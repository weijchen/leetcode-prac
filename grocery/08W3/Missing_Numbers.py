# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: count sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/missing-numbers
''' 
# --------------------------------------------------- libs import
import sys
from itertools import groupby
# len_a = int(input())
# arr_a = [int(i)for i in input().strip().split()]
# len_b = int(input())
# arr_b = [int(i)for i in input().strip().split()]

len_a = 10
arr_a = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
len_b = 13
arr_b = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]


keylis_b = [key for key, group in groupby(sorted(arr_b))]
counter_b = [len(list(group)) for key, group in groupby(sorted(arr_b))]
counter_a = [0 for i in range(len(keylis_b))]
for i in range(len(keylis_b)):
	for j in arr_a:
		if keylis_b[i] == j:
			counter_a[i] += 1
diff = []
for i in range(len(counter_a)):
	diff.append(counter_b[i] - counter_a[i])
for i in range(len(keylis_b)):
	if diff[i] != 0:
		print(keylis_b[i], end=' ')

