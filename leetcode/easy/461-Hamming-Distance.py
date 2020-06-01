# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 461, Created Nov. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/hamming-distance/description/
Tag: Bit Manipulation
''' 
# --------------------------------------------------- solution
'''
type(bin(x^y)) is 'str'
'''
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

