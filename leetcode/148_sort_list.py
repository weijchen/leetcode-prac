# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 148, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/sort-list/description/
''' 
# --------------------------------------------------- solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        lis = []
        while p != None:
            lis.append(p.val)
            p = p.next
        lis.sort()
        
        i = 0
        p = head
        while p != None:
            p.val=lis[i]
            i += 1
            p = p.next
        return head
