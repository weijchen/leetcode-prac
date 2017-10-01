# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 83, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/
''' 
# --------------------------------------------------- solution
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head