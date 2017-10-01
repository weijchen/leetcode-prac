# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 670, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/maximum-swap/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr = str(num)
        checksort = 0
        # check for no swap num
        for each in range(1, len(numstr)):
            print(numstr[each-1], numstr[each])
            if numstr[each-1] < numstr[each]:
                checksort += 1
        if checksort == 0:
            return num
        
        # other case
        max_ = max(set(numstr))
        change = 0
        while max_ == numstr[0]:
            numstr = numstr[1:]
            max_ = max(set(numstr))
            change += 1
        tempstr = str(num)[:change] 
        anslis = []
        for each in range(len(numstr)):
            idx = len(numstr) - 1 - each
            if numstr[idx] == max_:
                anslis.append(idx)
        numlis = [char for char in numstr]
        numlis[0], numlis[anslis[0]] = numlis[anslis[0]], numlis[0]

        return int(tempstr+''.join(numlis))
