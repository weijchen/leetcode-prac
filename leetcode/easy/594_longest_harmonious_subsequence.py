# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 594, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/longest-harmonious-subsequence/description/
Tag: Hash Table
''' 
# --------------------------------------------------- solution
'''
implementation of dictionary
dict.get(target, default value)
'''
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        int_dict = {}
        for i in nums:
            int_dict[i] = int_dict.get(i, 0) + 1
            
        ret = 0
        
        for key in int_dict:
            if key + 1 in int_dict:
                ret = max(int_dict[key] + int_dict[key + 1], ret)
        return ret