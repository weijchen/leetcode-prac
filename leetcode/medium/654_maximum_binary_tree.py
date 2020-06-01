# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 654, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/maximum-binary-tree/description/
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None:
            return null
        root.val = max(nums)
        idx = 0
        for each in range(len(nums)):
            if nums[each] == root:
                idx = each
                print(idx)
        leftnums = nums[:idx]
        rightnums = nums[idx+1:]

        root.left.value = constructMaximumBinaryTree(leftnums)
        root.right.value = constructMaximumBinaryTree(rightnums)
        # root.left = 
        # root.right = 
        
        
nums = [3,2,1,6,0,5]
r=Solution.constructMaximumBinaryTree(nums)
print(r)