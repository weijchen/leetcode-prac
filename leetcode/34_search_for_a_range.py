# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 34, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/search-for-a-range/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            start = nums.index(target)
            end = 0
            if len(nums) == 1:
                return [start, start]
            for idx in range(start, len(nums)):
                if nums[idx] == target:
                    end = idx
            return [start, end]
        except:
            return [-1, -1]

# --------------------------------------------------- formal solution
'''
Divide and conquer
'''
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        low, high = 0, len(nums) - 1
        result = []

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                result.append(mid)
                temp1 = mid + 1
                temp2 = mid - 1
                
                try:
                    while target == nums[temp1]:
                        result.append(temp1)
                        temp1 += 1
                except:
                    pass
                
                try:
                    while target == nums[temp2] and temp2 != -1:
                        result.append(temp2)
                        temp2 -= 1
                except: 
                    pass
                return [min(result), max(result)]

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return [-1, -1]