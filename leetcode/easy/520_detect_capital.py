# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 520, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/detect-capital/description/
Tag: String
''' 
# --------------------------------------------------- solution
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        check = 0
        
        for char in word:
            if ord(char) < 97:
                check += 1
        if check == len(word):
            return True
        elif check == 1 and ord(word[0]) < 97:
            return True
        elif check == 0:
            return True
        else:
            return False
# --------------------------------------------------- best solution
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        return word.isupper() or word.islower() or word.istitle()