# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 100, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/same-tree/description/
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p != None and q != None:
            if self.treetolis(p) == self.treetolis(q):
                return True
            else:
                return False
        elif p == None and q == None:
            return True
        else:
            return False
    def treetolis(self, tree):
        curlevel = [tree]
        strlevel = [tree.val]
        while curlevel:
            newlevel = []
            for each in curlevel:
                if each.left:
                    newlevel.append(each.left)
                    strlevel.append(each.left.val)
                else:
                    strlevel.append(0)
                if each.right:
                    newlevel.append(each.right)
                    strlevel.append(each.right.val)
                else:
                    strlevel.append(0)
            curlevel = newlevel
        return strlevel
# --------------------------------------------------- best solution
'''
Recursive solution
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        '''
        status = False
        
        if p is None and q is None:
            return True

        if p.val == q.val:
            status = True
            status = self.isSameTree(p.left, q.left)
            if status == True:
                status = self.isSameTree(p.right, q.right)
          
        return status
        '''
        #same as what i did above but more concise:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
          	return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
          
        return False
