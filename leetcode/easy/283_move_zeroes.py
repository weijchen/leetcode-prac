# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 283, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/move-zeroes/description/
Tag: Array, Two Pointers
''' 
# --------------------------------------------------- solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i += 1    
        zeroadd = length - len(nums)
        for each in range(zeroadd):
            nums.append(0)