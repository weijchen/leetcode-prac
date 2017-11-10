# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 136, Created Aug. 2017
Ver: 1.0
Link: https://leetcode.com/problems/single-number/description/
Tag: Hash table, Bit manipulation
''' 
# --------------------------------------------------- solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        list.sort(nums)
        for i in xrange(len(nums)):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i + 1] and nums[i] != nums[i - 1]:
                return nums[i]