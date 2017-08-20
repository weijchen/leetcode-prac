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

for i in range(1, n+1):
	space_num = n - i
	space = ' ' * space_num
	star_num = i
	star = '#' * star_num
	print(space + star)


# -- Awesome solution --
'''
one line code is powerful~~
'''
[print(' '*(n-i) + '#'*i) for i in range(1, n+1)]
