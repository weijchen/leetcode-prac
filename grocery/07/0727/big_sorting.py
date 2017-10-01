# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN:big sorting, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/big-sorting
''' 
# --------------------------------------------------- libs import
import sys

def sort(array):
	less = []
	equal = []
	greater = []
	if len(array) > 1:
		pivot = array[0]
		for x in array:
			if x < pivot:
				less.append(x)
			if x == pivot:
				equal.append(x)
			if x > pivot:
				greater.append(x)
		return sort(less) + equal + sort(greater)
	else:
		return array
n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = int(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
sort = sort(unsorted)
for i in range(len(sort)):
    print(sort[i])