# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 496, Created Nov. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/next-greater-element-i/description/
Tag: Stack
''' 
# --------------------------------------------------- solution
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = []
        for each in findNums:
            for i in range(nums.index(each), length):
                if i == len(nums)-1:
                    if nums[i] > each:
                        ans.append(nums[i])
                    else:
                        ans.append(-1)
                elif nums[i] > each:
                    ans.append(nums[i])
                    break
        return ans
# --------------------------------------------------- better solution
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        ans = []
        
        for x in nums:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in findNums:
            ans.append(d.get(x, -1))
            
        return ans