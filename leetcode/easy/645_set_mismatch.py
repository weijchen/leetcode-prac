# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 645, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/set-mismatch/description/
Tag: Hash Table, Math
''' 
# --------------------------------------------------- solution
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        mem = [each for each in range(1, len(nums)+1)]
        
        nums.sort()
        anslis = []
        while len(anslis) < 1:
            for each in nums:
                if each in mem:
                    mem.pop(mem.index(each))
                else:
                    anslis.append(each)
        return anslis + mem
# --------------------------------------------------- reference solution
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dup_num = 0
        miss_num = 0
        num_dict = {}
        
        for num in nums:
            if (num in num_dict):
                dup_num = num
            else:
                num_dict[num] = 1
                
        for i in range(0, len(nums) + 1):
            if (i not in num_dict):
                miss_num = i
                
        return [dup_num, miss_num]