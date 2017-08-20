# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: quick sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/quicksort1?h_r=next-challenge&h_v=zen
''' 
# --------------------------------------------------- libs import
def quick_sort(l):
	less = []
	equal = []
	greater = []
	pivot = l[0]
	for i in l:
		if i > pivot:c
			greater.append(i)
		elif i < pivot:
			less.append(i)
		else:
			equal.append(i)
	return less + equal + greater
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
ar = quick_sort(ar)
print(" ".join(map(str,ar)))