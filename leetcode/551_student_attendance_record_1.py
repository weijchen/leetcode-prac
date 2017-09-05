# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 551, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/student-attendance-record-i/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) > 0:
            late_score = 0
            absent_score = 0
            for each in s:
                if each == 'A':
                    late_score = 0
                    absent_score += 1
                    if absent_score == 2:
                        return False
                elif each == 'L':
                    late_score += 1
                    if late_score == 3:
                        return False
                elif each == 'P':
                    late_score = 0
            return True
        else:
            return False
# --------------------------------------------------- best solution
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = s.count('A') > 1 or s.count('LLL') >= 1
        return True if not check else False