# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 500, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/keyboard-row/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def findWords(words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line_1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        line_2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        line_3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        for each in words:
            scorelis = [0] * 3
            for char in each:
                char = char.lower()
                if char in line_1:
                    scorelis[0] += 1
                elif char in line_2:
                    scorelis[1] += 1
                else:
                    scorelis[2] += 1
            if (scorelis[0] != 0 and scorelis[1] == 0 and scorelis[2] == 0) or (scorelis[0] == 0 and scorelis[1] != 0 and scorelis[2] == 0) or (scorelis[0] == 0 and scorelis[1] == 0 and scorelis[2] != 0):
                return each

                # return each


r = Solution.findWords(["Hello", "Alaska", "Dad", "Peace"])
# print(r)