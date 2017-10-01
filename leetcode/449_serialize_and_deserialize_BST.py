# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 449, Created Aug. 2017
Ver: 1.0 (not finish)
Link: 
''' 
# --------------------------------------------------- solution
# Definition for a binary tree node.
from tree_helper import Tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        curlevel = [root]
        strlis = [str(root.val)]
        while curlevel:
            nextlevel = []
            for each in curlevel:
                if each.left:
                    nextlevel.append(each.left)
                    strlis.append(str(each.left.val))
                if each.right:
                    nextlevel.append(each.right)
                    strlis.append(str(each.right.val))
            curlevel = nextlevel

        return ' '.join(strlis)
        # return strlis

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        data = [int(each) for each in data]
        print(data)

        data.insert(0, 0)
        root = TreeNode(data[1])
        for each in range(1, len(data)):
            data[each] = TreeNode(data[each])
            if each*2 < len(data):
                data[each].left = data[each*2]
            else:
                data[each].left = None
            if each*2+1 < len(data):
                data[each].right = data[each*2+1]
            else:
                data[each].right = None
        return root



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
leaf_4, leaf_5, leaf_6, leaf_7 = TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
root.left.left = leaf_4
root.left.right = leaf_5
root.right.left = leaf_6
root.right.right = leaf_7
codec = Codec()
str_ = codec.serialize(root)
print(str_)
tree = Tree(str_)
root = tree.root
print(root.left.val)