# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 682, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/baseball-game/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        sum_ = 0
        buff = []
        for each in ops:
            if each == 'D':
                buff.append(int(buff[-1])*2)
            elif each == 'C':
                buff.pop(-1)
            elif each == '+':
                buff.append(int(buff[-2])+ int(buff[-1]))
            else:
                buff.append(int(each))
        for each in buff:
            sum_ += each
        return sum_