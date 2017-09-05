# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 121, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or len(prices) == 1:
            return 0
        else:
            profit = 0
            profitlis = []
            for each in range(1, len(prices)):
                test1 = prices[each]
                test2 = prices[each-1]
                if test1 > test2:
                    buy = prices[each-1]
                    idx = prices.index(buy)
                    selllis = prices[idx+1:]
                    for sell in selllis:
                        if sell > buy:
                            profitlis.append(sell-buy)
            if len(profitlis) == 0:
                return 0
            else:
                return max(profitlis)