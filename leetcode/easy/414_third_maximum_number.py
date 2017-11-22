# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 414, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/third-maximum-number/description/
Tag: Array
''' 
# --------------------------------------------------- solution
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return max(nums)
        return nums[-3]
