# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 231, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/power-of-two/description/
Tag: Math, Bit manipulation
''' 
# --------------------------------------------------- solution
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        else:
            if n == 1:
                return True
            else:
                x = str(bin(n)).count('1')
                if x == 1:
                    return True
                else:
                    return False
# --------------------------------------------------- best solution
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        return (n&(n-1))==0
        