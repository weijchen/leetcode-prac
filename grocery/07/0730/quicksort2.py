# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: quick sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/quicksort2?h_r=next-challenge&h_v=zen
''' 
# --------------------------------------------------- libs import
def quick_sort(l):
	less = []
	equal = []
	greater = []
	pivot = l[0]
	for i in l:
		if i > pivot:
			greater.append(i)
		elif i < pivot:
			less.append(i)
		else:
			equal.append(i)
	if len(less) > 1:
		less = quick_sort(less)
		print(" ".join(map(str,less)))
	if len(greater) > 1:
		greater = quick_sort(greater)
		print(" ".join(map(str,greater)))
	return less + equal + greater
# m = 7
# ar = [5, 8, 1, 3, 7, 9, 2]
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
ar = quick_sort(ar)
print(" ".join(map(str,ar)))
