# -*- coding: utf-8 -*-
'''
Link: https://leetcode.com/problems/reverse-integer/description/
Tag: Math
''' 
# --------------------------------------------------- solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
				# Perform the reverse
				x_rev = str(x)
				if x_rev[0] == '-':
					x_rev = int('-'+x_rev[::-1][:-1])
				else:
					x_rev = int(x_rev[::-1])

				# Check int range
				if x_rev > 2**31-1 or x_rev < -1*2**31:
					return 0
				else:
					return x_rev

