# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 654, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/merge-sorted-array/description/
Tag: Array, Two Pointers
''' 
# --------------------------------------------------- solution
class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()

r = Solution.merge([1],1,[],0)
print(r)