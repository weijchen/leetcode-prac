# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 219, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/contains-duplicate-ii/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 35000:
            return False
        for idx in range(len(nums)):
            for dis in range(1, k+1):
                try:
                    if nums[idx] == nums[idx+dis]:
                        return True
                except:
                    pass
        return False
# --------------------------------------------------- best solution
'''
Use dictionary to store the idx of num's appearance
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k:
                    return True
            dic[nums[i]] = i
        return False