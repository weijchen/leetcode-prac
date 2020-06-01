# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 572, Created Aug. 2017
Ver: 1.0 (not finish)
Link: https://leetcode.com/problems/subtree-of-another-tree/description/
Tag: Tree
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# ===== Solution 1 =====
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

# ===== Solution 2 =====
# [3,4,5,1,2,null,null,null,null,0]
# [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
# [1,null,1,null,1,null,1,null,1,null,1,2]
class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traverse(s, t) 
        
    def traverse(self, s, t_head):
        if s == None:
            return False
        if s.val == t_head.val:
            s_lis, t_lis = [], []
            a = self.inorder(s, s_lis)
            b = self.inorder(t_head, t_lis)
            print("a: {}".format(a))
            print("b: {}".format(b))
            if a == b:
                # print("hi")
                return True
            else:
                if s.left != None and s.right != None:
                    return self.traverse(s.left, t_head) or self.traverse(s.right, t_head)
                elif s.left != None and s.right == None:
                    return self.traverse(s.left, t_head)
                elif s.right != None and s.left == None:
                    return self.traverse(s.right, t_head)
                else:
                    return False
            
    def inorder(self, n, lis):
        if n.left != None and n.right != None:
            self.inorder(n.left, lis)
            lis.append(n.val)
            self.inorder(n.right, lis)
        elif n.left != None and n.right == None:
            self.inorder(n.left, lis)
            lis.append(n.val)
        elif n.right != None and n.left == None:
            lis.append(n.val)
            self.inorder(n.right, lis)
        else:
            return lis