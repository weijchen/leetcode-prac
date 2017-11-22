# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 171, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/excel-sheet-column-number/description/
Tag: Math
''' 
# --------------------------------------------------- solution
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlis = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = 0
        for char in xrange(len(s)):
            pos_char = len(s)-1-char
            num += ((strlis.index(s[char]) + 1) * 26 ** pos_char)
        return num
        