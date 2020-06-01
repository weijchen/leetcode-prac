# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 693, Created Jan. 2018
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/binary-number-with-alternating-bits/description/
Tag: Bit Manipulation
''' 
# --------------------------------------------------- solution
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        order_2 = bin(n)[2:]
        for _ in range(len(order_2)-1):
            if order_2[_] == order_2[_+1]:
                return False
        return True

