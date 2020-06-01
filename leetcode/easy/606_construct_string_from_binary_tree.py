# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 606, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/construct-string-from-binary-tree/description/
Tag: String, Tree
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t == None:
            return ''
        elif t.left != None and t.right == None:
            return '{0}({1})'.format(t.val, self.tree2str(t.left))
        elif t.left == None and t.right != None:
            return '{0}()({1})'.format(t.val, self.tree2str(t.right))
        elif t.left != None and t.right != None:
            return '{0}({1})({2})'.format(t.val, self.tree2str(t.left), self.tree2str(t.right))
        else:
            return '{}'.format(t.val)