# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 387, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/
Tag: 
''' 
# --------------------------------------------------- solution
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 0:
            for each in s:
                check = each
                idx = s.index(check)
                checkarr = s[idx+1:]
                if check not in checkarr:
                    return idx
            return -1
        else:
            return -1

# --------------------------------------------------- best solution
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = []
        for ch in set(s):
            if s.find(ch) == s.rfind(ch):
                index.append(s.find(ch))
        return min(index) if index else -1