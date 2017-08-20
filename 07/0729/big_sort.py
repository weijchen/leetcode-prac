# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: big sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/big-sorting
''' 
# --------------------------------------------------- libs import
#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)

def sort(array):
    equal = []
    less = []
    greater = []
    if len(array) > 1:
    	divider = array[0]
    	for x in array:
    		print(x)
    		if x < divider:
    			less.append(x)
    		elif x > divider:
    			greater.append(x)
    		else:
    			equal.append(x)
    	return sort(less) + equal + sort(greater)
    else:
    	return array

def sort(array):
	'''
	bucket sort, 
	'''

bucket = {}
for number in unsorted:
	length = len(i)
	bucket

sort = sort(unsorted)
print(sort)