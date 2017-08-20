# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: insertion sort part.2, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/insertionsort2/problem
''' 
# --------------------------------------------------- libs import
import sys

n = int(input())
unsorted = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def sort(array, i):
	new = sorted(array[:i+1]) + array[i+1:]
	return ' '.join(str(v) for v in new)

for i in range(1, n):
	print(sort(unsorted, i))
