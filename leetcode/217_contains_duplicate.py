# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 217, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/contains-duplicate/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mem = {}
        for each in nums:
            if each not in mem:
                mem[each] = 1
            else:
                return True
        return False
            
        