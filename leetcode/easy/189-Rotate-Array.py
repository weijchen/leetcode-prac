# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 122, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
Tag: Array, Greedy
''' 
# --------------------------------------------------- solution
'''
Operation in array structure (pop, insert(idx, value))
'''
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            while k > 0:
                temp = nums.pop(-1)
                nums.insert(0, temp)
                k = k-1