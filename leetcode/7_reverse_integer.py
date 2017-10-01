# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 7, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/reverse-integer/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        abs_x = abs(x)
        strint = str(abs_x)
        reverse_int = int(''.join([str(strint[each]) for each in range(len(strint)-1, -1, -1)]))
        if reverse_int > 2 ** 31:
            return 0
        else:
            if x < 0:
                return reverse_int * -1
            return reverse_int