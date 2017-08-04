# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: cake candles, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/birthday-cake-candles?h_r=next-challenge&h_v=zen
''' 
# --------------------------------------------------- libs import
# #!/bin/python

import sys

def birthdayCakeCandles(n, ar):
	array = list(ar)
	target = max(array)
	count = 0
	for i in range(0, n):
		if array[i] == target:
			count += 1
	print(count)
    # Complete this function

n = int(input().strip())
ar = map(int, input().strip().split(' '))
result = birthdayCakeCandles(n, ar)

# -- Great solution --
n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

print(height.count(max(height)))