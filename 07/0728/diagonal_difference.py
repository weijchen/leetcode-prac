# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: diagonal difference, Created Jul. 2017
Ver: 1.0 (finish)
Link: https://www.hackerrank.com/challenges/plus-minus
''' 
# --------------------------------------------------- libs import
n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

primary_d = 0
secondary_d = 0
for i in range(0, n):
	primary_d = primary_d + a[i][i]
	secondary_d = secondary_d + a[i][n-i-1]
print(abs(primary_d - secondary_d))