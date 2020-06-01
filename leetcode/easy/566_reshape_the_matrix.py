# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 566, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/reshape-the-matrix/description/
Tag: Array
''' 
# --------------------------------------------------- solution
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        old_r = len(nums)
        old_c = len(nums[0])
        lis = [j for i in nums for j in i]
        anslis = []
        if old_r*old_c == r*c:
            for each in range(r):
                sublis = lis[0+each*c:(each+1)*c]
                anslis.append(sublis)
        else:
            return nums
        return anslis