# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: mini-max_sum, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/mini-max-sum
''' 
# --------------------------------------------------- libs import
#!/bin/python

import sys

def sort(array):
	for i in range(len(array)-1):
		if array[i] > array[i+1]:
			temp = array[i]
			array[i] = array[i+1]
			array[i+1] = temp
			sort(array)
	return array	


arr = list(map(int, input().strip().split(' ')))
arr = sort(arr)
total = sum(arr)
maxi = total - arr[0]
mini = total - arr[4]
print('{} {}'.format(total - arr[4], total - arr[0]))
