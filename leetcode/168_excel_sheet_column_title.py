# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 168, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/excel-sheet-column-title/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        strlis = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if n == 0:
            return ""
        max_ = 0
        power = 1
        while max_ < n:
            max_ += 26 ** power
            power += 1

        count = power - 2
        anslis = []
        for each in xrange(count, -1, -1):
            multiplier = n /(26 ** each)
            if each == 0:
                anslis.append(strlis[multiplier-1])
                return ''.join(anslis)
            if n % 26 == 0:
                anslis.append(strlis[multiplier - 1-1])
                n -= (multiplier -1) * 26 ** each
            else:
                anslis.append(strlis[multiplier-1])
                n -= multiplier * 26 ** each
