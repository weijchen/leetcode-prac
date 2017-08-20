# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: cake candles, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/time-conversion?h_r=next-challenge&h_v=zen
''' 
# --------------------------------------------------- libs import
#!/bin/python

import sys

def timeConversion(s):
	if s[-2:] == 'PM' and s[:2] != '12':
		new = str(str(int(s[:2]) + 12) + s[2:-2])
		print(new)
	elif s[-2:] == 'AM' and s[:2] == '12':
		new = str(str('00' + s[2:-2]))
		print(new)
	else:
		print(s[:-2])

s = input().strip()
result = timeConversion(s)
