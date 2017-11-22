# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 70, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/climbing-stairs/description/
Tag: Dynamic Programming
''' 
# --------------------------------------------------- solution
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Fibonacci
        '''
        mem = {0:0, 1:1, 2:2}
        for each in range(n+1):
            if each not in mem.keys():
                mem[each] = mem[each-1] + mem[each-2]
        return mem[n]