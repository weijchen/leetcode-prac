# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 669, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/trim-a-binary-search-tree/description/
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def isLeaf(root):
            return root.left == None and root.right == None
        
        while root == None:
            return
        
        if isLeaf(root):
            if (L > root.val) or (R < root.val):
                return None
            else:
                return root
        
        if L <= root.val <= R:
            root.right = self.trimBST(root.right, L, R)
            root.left = self.trimBST(root.left, L, R)
            return root
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            return self.trimBST(root.left, L, R)
            
# --------------------------------------------------- best solution
class Solution(object):
    def trimBST(self, root, L, R):
        if root is None:
          return None

        if root.val < L:
          return self.trimBST(root.right, L, R)

        if root.val > R:
          return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root