# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 504, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/base-7/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maxseven(self, num):
        count = 1
        while num / 7 > 6:
            count += 1
            num = num / 7
        return count
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return str(0)
        negcheck = False
        if num > 0:
            negcheck = True
            
        num = abs(num)
        seven = self.maxseven(num)
        sevenlis = [7**seven for seven in range(self.maxseven(num)+1)]
        anslis = [0]*len(sevenlis)
        for each in range(len(sevenlis)-1, -1, -1):
            count = 0
            while num >= sevenlis[each]:
                num -= sevenlis[each]
                count += 1
            anslis[len(anslis)-1-each] = str(count)
        if negcheck:
            if anslis[0] == '0':
                return ''.join(anslis[1:])
            return ''.join(anslis)
        else:
            if anslis[0] == '0':
                return '-'+''.join(anslis[1:])
            return '-'+''.join(anslis)