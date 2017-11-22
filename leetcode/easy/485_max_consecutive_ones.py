# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 485, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/max-consecutive-ones/description/
Tag: Array
''' 
# --------------------------------------------------- solution
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        ans = 0
        for num in nums:
            if num == 1:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        return ans