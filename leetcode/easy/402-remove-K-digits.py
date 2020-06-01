# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 205, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/isomorphic-strings/description/
Tag: Has Table
''' 
# --------------------------------------------------- solution
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """  
        if k == len(num):
            return "0"
        remove = 0
        nums = [n for n in num]
        nums = nums + ['0']
        while remove < k:
            for idx in range(1, len(nums)):
                if nums[idx] < nums[idx-1]:
                    nums.pop(idx-1)
                    break
                if idx == len(nums):
                    nums.pop(idx)
            remove += 1
        return str(int("".join(nums[:-1])))
# --------------------------------------------------- best solution
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out = []
        for d in num:
            while k and out and out[-1] > d:
                out.pop()
                k -= 1
            out.append(d)
        return ''.join(out[:-k or None]).lstrip('0') or '0'
