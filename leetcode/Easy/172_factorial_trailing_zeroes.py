# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 172, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/factorial-trailing-zeroes/description/
Tag: Math
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maxfive(self, n):
        count = 1
        while n / 5 > 4:
            count += 1
            n = n / 5
        return count
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if 0 <= n < 5:
            return 0
        fivelis = self.maxfive(n)
        ans = 0
        for five in range(1, fivelis+1):
            ans += (n/5**five)
        return ans