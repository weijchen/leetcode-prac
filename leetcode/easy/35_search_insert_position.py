# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 35, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/search-insert-position/description/
Tag: Array, Binary Search
''' 
# --------------------------------------------------- solution
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([idx for idx in range(len(nums)) if nums[idx] < target])