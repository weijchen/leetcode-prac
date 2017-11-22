# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 482, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/license-key-formatting/description/
''' 
# --------------------------------------------------- solution
'''
can use replace() function
'''
class Solution(object):
    def trans(self, string, K):
        dash_count = 0
        templis = []
        for each in string:
                if type(each) == str:
                    templis.append(each.upper())
                else:
                    templis.append(each)
                dash_count += 1
                while dash_count == K:
                    templis.append('-')
                    dash_count = 0
        return templis
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        count = 0
        strlis = []
        anslis = []
        for char in S:
            if char != '-':
                count += 1
                strlis.append(str(char))
        if count % K == 0:
            anslis = self.trans(strlis, K)
        else:
            minus = count % K
            anslis_0 = strlis[:minus]
            anslis_1 = []
            for each in anslis_0:
                if type(each) == str:
                    anslis_1.append(each.upper())
                else:
                    anslis_1.append(each)
            strlis = strlis[minus:]
            anslis = self.trans(strlis, K)
            anslis = anslis_1 + ['-']+ anslis
        return ''.join(anslis[:-1])
# --------------------------------------------------- best solution
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = S.upper().replace('-', '')
        first = K if not len(s)%K else len(s)%K
        res = s[:first]
        while first < len(s):
            res += '-' + s[first:first+K]
            first+=K
        return res