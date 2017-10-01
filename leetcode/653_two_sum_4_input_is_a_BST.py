# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 653, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        mem = {}
        anslis = self.bfs(root)
        bfs, s = [root], set()

        for i in bfs:
        	if i.left: bfs.append(i.left)
        	if i.right: bfs.append(i.right)
        	
        for each in anslis:
            if (k - each) in mem:
                return True
            else:
                mem[each] = k - each
        return False
        
    def bfs(self, root):
        curlis = [root]
        strlis = [root.val]
        while curlis:
            nextlis = []
            for each in curlis:
                if each.left:
                    nextlis.append(each.left)
                    strlis.append(each.left.val)
                if each.right:
                    nextlis.append(each.right)
                    strlis.append(each.right.val)
            curlis = nextlis
        return strlis
# --------------------------------------------------- best solution
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        bfs, s = [root], set()
        
        for i in bfs:
            if k-i.val in s: return True
            s.add(i.val)
            if i.left: bfs.append(i.left)
            if i.right: bfs.append(i.right)
        return False