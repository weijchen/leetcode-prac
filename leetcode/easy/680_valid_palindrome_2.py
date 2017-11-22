# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 680, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/valid-palindrome-ii/description/
Tag: String
''' 
# --------------------------------------------------- solution
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        slis = [char for char in s]
        length = len(slis) // 2
        if self.checkpalindrome(slis):
            return True
        else:
            for idx in range(length):
                start = s[idx]
                end = s[len(slis)-(idx+1)]
                if start != end:
                    lis_1 = [each for each in slis]
                    lis_2 = [each for each in slis]
                    lis_1.pop(idx)
                    lis_2.pop(len(slis)-(idx+1))
                    if self.checkpalindrome(lis_1) or self.checkpalindrome(lis_2):
                        return True
                    return False

    
    def checkpalindrome(self, s):
        if s == s[::-1]:
            return True
        return False
        # length = len(s) // 2
        # for idx in range(length):
        #     if s[idx] != s[len(s)-(idx+1)]:
        #         return False
        # return True