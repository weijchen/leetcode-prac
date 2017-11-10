# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 205, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/isomorphic-strings/description/
Tag: Hash table
''' 
# --------------------------------------------------- solution
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mem = {}
        for idx in xrange(len(s)):
            if s[idx] not in mem:
                mem[s[idx]] = t[idx]
            else:
                if mem[s[idx]] != t[idx]:
                    return False
        mem = {}
        for idx in xrange(len(t)):
            if t[idx] not in mem:
                mem[t[idx]] = s[idx]
            else:
                if mem[t[idx]] != s[idx]:
                    return False
        return True