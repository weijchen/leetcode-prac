# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 557, Created Oct. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
Tag: String
''' 
# --------------------------------------------------- solution
'''
Use buffer to store split word(reversed)
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis = [char for char in s] + [" "]
        buff = []
        anslis = []
        for each in lis:
            if each == ' ':
                anslis.append(''.join(buff[::-1]))
                buff = []
            else:
                buff.append(each)
        return ' '.join(anslis)
# --------------------------------------------------- best solution
class Solution(object):
    def reverseWords(self, s):
        buffer = s.split()
        buffer = [i[::-1] for i in buffer]
        return " ".join(buffer)