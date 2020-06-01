# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 16, Created Nov. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/3sum-closest/description/
Tag: Array, Two Pointers
''' 
# --------------------------------------------------- solution
'''
O(n^3) algorithm, exceed time limit
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)
        test = abs(target - (nums[0] + nums[1] + nums[2]))
        ans = nums[0] + nums[1] + nums[2]
        for each1 in range(len(nums)):
            p1 = nums[each1]
            remain1 = nums[:each1] + nums[each1+1:]
            for each2 in range(len(remain1)):
                p2 = remain1[each2]
                remain2 = remain1[:each2]+remain1[each2+1:]
                for each3 in range(len(remain2)):
                    p3 = remain2[each3]
                    temp = abs(target - (p1 + p2 + p3))
                    if temp < test:
                        test = temp
                        ans = p1 + p2 + p3
        return ans
# --------------------------------------------------- solution
'''
O(n^2) algorithm, use two pointers
'''
