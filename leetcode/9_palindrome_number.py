# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 9, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/palindrome-number/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x % 10 == 0 and x != 0 or x < 0:
            return False
        if 0 <= x <= 9:
            return True
        reverted = 0
        while x > 0:
            reverted *= 10
            reverted += x % 10
            if reverted == x:
                return True
            else:
                x /= 10
                if reverted == x:
                    return True
        return False