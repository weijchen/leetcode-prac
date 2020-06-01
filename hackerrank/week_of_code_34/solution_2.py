#!/bin/python3
# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Week of code 34, Created Jul. 2017
Ver: 1.1 (gcd, sort, set)
Link: 
''' 
# --------------------------------------------------- libs import
import sys
# --------------------------------------------------- solution
def gcd(x, y):
	if x < y:
		x, y = y, x
	remain = x % y
	if remain == 0:
		return y
	else:
		x, y = y, remain
		return gcd(x, y)

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
			
def maximumGcdAndSum(A, B):
	C = sort(list(set(A) & set(B)))
	if len(C) >= 1:
		sumlis = sort(A + B)
		gcd_temp = C[-1]
		sum_temp = C[-1] * 2
		for i in range(n - 1, -1, -1):
			var_1 = sumlis[i]
			# run when var_1 larger than GCD
			if var_1 > gcd_temp:
				solution = var_1 + gcd_temp
				GCD = gcd(var_1, gcd_temp)
				if GCD > gcd_temp:
					gcd_temp = GCD
					sum_temp = solution
				elif GCD == gcd_temp:
					if solution > sum_temp:
						sum_temp = solution
			else:
				pass
		print(sum_temp)
	else:
		gcd_temp = 1
		sum_temp = 1
		A = sort(A)
		B = sort(B)
		for i in range(n - 1, -1, -1):
			var_1 = A[i]
			if var_1 > gcd_temp:
				for j in range(n - 1, -1, -1):
					var_2 = B[j]
					if var_2 > gcd_temp:
						solution = A[i] + B[j]
						GCD = gcd(var_1, var_2)
						if GCD > gcd_temp:
							gcd_temp = GCD
							sum_temp = solution
						elif GCD == gcd_temp:
							if solution > sum_temp:
								sum_temp = solution
					else:
						pass
			else:
				pass
		print(sum_temp)
	
n = 5
A = [11, 1, 4, 100, 1000]
B = [5, 2, 12, 8, 3]
# A = [3, 1, 4, 2, 8]
# B = [5, 2, 12, 8, 3]
# n = int(input().strip())
# A = list(map(int, input().strip().split(' ')))
# B = list(map(int, input().strip().split(' ')))
maximumGcdAndSum(A, B)
