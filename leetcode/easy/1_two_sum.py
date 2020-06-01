# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
Link: https://leetcode.com/problems/two-sum/description/
Tag: Array, Hash table
''' 
# --------------------------------------------------- solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for idx in xrange(len(nums)):
            dividelis = nums[idx+1:]
            for each in xrange(len(dividelis)):
                if nums[idx] + dividelis[each] == target:
                    return (idx, idx+each+1)

# --------------------------------------------------- best solution
# O(n) method, use dict to store different first, if diff exist, return
'''
use hash table: create a relation dict that can represent answer and input's relation, 
help improve searching efficiency
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        dict = {}
				for i, n in enumerate(nums):
					if n in dict:
						return [dict[n], i]
					dict[target-n] = i
