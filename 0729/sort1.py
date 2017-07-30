# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: insertion sort part.1, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/insertionsort1/problem
''' 
# --------------------------------------------------- libs import
import sys

n = int(input())
unsorted = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def sort(array, n):
	target = array[n-1]
	for i in range(1, n):
		if array[n-1-i] > target:
			array[n-1-i+1] = array[n-1-i]
			values = ' '.join(str(v) for v in array)
			print(values)
			if n-1-i == 0:
				array[n-1-i] = target
				values = ' '.join(str(v) for v in array)
				print(values)
				break
		else:
			array[n-i] = target
			values = ' '.join(str(v) for v in array)
			print(values)
			break




sort_arr = sort(unsorted, n)
