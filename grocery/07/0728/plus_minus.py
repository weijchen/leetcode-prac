# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: diagonal difference, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/plus-minus
''' 
# --------------------------------------------------- libs import
import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

pos = 0
neg = 0
zero = 0
for i in range(0, n):
    if arr[i] > 0:
        pos += 1
    elif arr[i] < 0:
        neg += 1
    else:
        zero += 1
print("{:6f}".format(pos/n))
print("{:6f}".format(neg/n))
print("{:6f}".format(zero/n))
    