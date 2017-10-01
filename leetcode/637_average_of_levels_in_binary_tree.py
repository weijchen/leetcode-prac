# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 637, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        curlis = [root]
        anslis = []
        while curlis:
            nextlis = []
            s, length = 0.0, len(curlis)    # set s to 0.0, can avoid float problem
            for each in curlis:
                s += each.val
                if each.left: nextlis.append(each.left)
                if each.right: nextlis.append(each.right)
            curlis = nextlis
            anslis.append(s/length)
        return anslis