# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 78, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/subsets/description/
Tag: Array, Backtracking, Bit Manipulation
''' 
# --------------------------------------------------- solution
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        bitmap = 2**len(nums)
        binlis = []
        anslis = []
        for each in xrange(bitmap):
            each = bin(each)[2:]
            while len(each) != len(nums):
                each = '0' + each
            binlis.append(each)
        for each in binlis:
            ans = []
            for char in range(len(each)):
                if each[char] == '1':
                    ans.append(nums[char])
            anslis.append(ans)
        return anslis