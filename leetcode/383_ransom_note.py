# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 383, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/ransom-note/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rlis = list(ransomNote)
        mlis = list(magazine)
        for char in rlis:
            if char not in mlis:
                return False
            if char in mlis:
                mlis.pop(mlis.index(char))
        return True
        
# --------------------------------------------------- best solution
'''
Compare count of two lists
'''
import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True