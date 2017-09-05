# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 598, Created Aug. 2017
Ver: 1.0
Link: https://leetcode.com/problems/range-addition-ii/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        rowlis = []
        collis = []
        if ops == []:
            return m*n
        else:
            for each in ops:
                rowlis.append(each[0])
                collis.append(each[1])
            return min(rowlis)*min(collis)
# --------------------------------------------------- best solution
'''
use array complement
'''
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        rowlis = []
        collis = []
        if ops == []:
            return m*n
        else:
            return min(each[0] for each in ops)*min(each[1] for each in ops)