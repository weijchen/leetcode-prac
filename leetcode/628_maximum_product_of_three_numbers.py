# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 628, Created Sep. 2017
Ver: 1.0
Link: https://leetcode.com/problems/maximum-product-of-three-numbers/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_ = nums[-1]
        first_2 = nums[0]*nums[1]
        end_2 = nums[-2]*nums[-3]
        if first_2> end_2:
            return max_ * first_2
        return max_ * end_2
        