# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 671, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
''' 
'''
Breadth-first search
'''
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curlevel = [root]
        vallis = [root.val]
        while curlevel:
            nextlevel = []
            for each in curlevel:
                if each.left:
                    nextlevel.append(each.left)
                    vallis.append(each.left.val)
                if each.right:
                    nextlevel.append(each.right)
                    vallis.append(each.right.val)
            curlevel = nextlevel
        anslis = sorted(set(vallis))
        if len(anslis) == 1:
            return -1
        else:
            return anslis[1]
        