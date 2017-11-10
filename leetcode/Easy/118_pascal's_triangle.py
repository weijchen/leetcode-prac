# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 118, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/pascals-triangle/description/
Tag: Array
''' 
# --------------------------------------------------- solution
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        anslis = []
        curarr = [1]
        if numRows > 0:
            anslis.append(curarr)
        for row in range(1, numRows):
            empty = [0]*(row+1)
            for each in range(len(curarr)):
                empty[each] += curarr[each]
                empty[each+1] += curarr[each]
            curarr = empty
            anslis.append(empty)
        return anslis