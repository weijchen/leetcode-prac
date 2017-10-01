# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 169, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/majority-element/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        amount = len(nums)
        if amount == 1:
            return nums[0]
        
        temp = nums[0]
        dict = {}
        for each in xrange(1, len(nums)):
            if nums[each] not in dict.keys():
                dict[nums[each]] = nums.count(nums[each])
        return max(dict, key = lambda i: dict[i])