# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 122, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
Tag: Array, Greedy
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for idx in range(1, len(prices)):
            if prices[idx]> prices[idx-1]:
                profit += prices[idx] - prices[idx-1]
            
        return profit