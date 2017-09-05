# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 400, Created Aug. 2017
Ver: 1.0 ()
Link: https://leetcode.com/problems/nth-digit/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        else:
            lengthmem = [9, 180, 2700, 36000, 450000, 5400000, 63000000, 720000000, 8100000000]
            check = 0
            digit = 0
            for each in lengthmem:
                if check < n:
                    check += each
                    digit = lengthmem.index(each) + 1
            print(check, digit)
        # lis = ''.join([str(each) for each in range(1, 10 ** digit)])
        # return int(lis[n-1])
        