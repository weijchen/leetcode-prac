# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 58, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/length-of-last-word/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        charlis = [char for char in s]
        count = 0
        idx = len(charlis)
        countlis = []
        if s == "":
            return 0
        for idx in range(len(charlis)):
            if charlis[idx] == ' ':
                countlis.append(count)
                count = 0
            elif idx == len(charlis)-1:
                count += 1
                countlis.append(count)
            else:
                count += 1
        for each in range(len(countlis)-1, -1, -1):
            if countlis[each] != 0:
                return countlis[each]
        return 0
# --------------------------------------------------- best solution
'''
Use built-in split function to divide specific char or spaces
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s.split()) == 0 else len(s.split()[-1])