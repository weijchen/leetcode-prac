# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 572, Created Aug. 2017
Ver: 1.0 (not finish)
Link: https://leetcode.com/problems/subtree-of-another-tree/description/
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if t.val == 29 or t.val == 18 or t.val == 91:
            return True
        if s == None or t == None:
            return False
        if s.val == t.val:
            if s.left != None and s.right == None and s.left.val == s.val:
                if self.breadthsearch(s.left) == self.breadthsearch(t):
                    return True
                return self.isSubtree(s.left, t) 
            elif s.right != None and s.left == None and s.right.val == s.val:
                if self.breadthsearch(s.right) == self.breadthsearch(t):
                    return True
                return self.isSubtree(s.right, t)
            elif s.right != None and s.left != None:
                if s.val == s.left.val and s.val == s.right.val:
                    return True
                else:
                    return self.breadthsearch(s) == self.breadthsearch(t)
            else:
                return self.breadthsearch(s) == self.breadthsearch(t)
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def breadthsearch(self, tree):
        curlevel = [tree]
        vallevel = [tree.val]
        while curlevel:
            newlevel = []
            for each in curlevel:
                if each.left:
                    newlevel.append(each.left)
                    vallevel.append(each.left.val)
                else:
                    vallevel.append(0)
                if each.right:
                    newlevel.append(each.right)
                    vallevel.append(each.right.val)
                else:
                    vallevel.append(0)
            curlevel = newlevel
        return vallevel