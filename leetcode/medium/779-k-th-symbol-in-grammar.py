# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 779, Created Feb. 2018
Ver: 1.0 (finish)
Link: https://leetcode.com/contest/weekly-contest-70/problems/k-th-symbol-in-grammar/
''' 
# --------------------------------------------------- solution
def kthGrammar(N, K):
    """
    :type N: int
    :type K: int
    :rtype: int
    """
    record = 0
    while K > 1:
        if K % 2 == 0:
            K /= 2
            if record == 0:
                record = 1
            else:
                record = 0
        else:
            K = (K-1)/2+1
    return record