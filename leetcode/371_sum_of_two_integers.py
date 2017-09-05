# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 551, Created Aug. 2017
Ver: 1.0
Link: https://leetcode.com/problems/sum-of-two-integers/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        lis_a = (a, b)
        lis_b = (1, 1)
        return sum(p*q for p,q in zip(lis_a, lis_b))