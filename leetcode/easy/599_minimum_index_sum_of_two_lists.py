# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 599, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
Tag: Hash Table
''' 
# --------------------------------------------------- solution
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = {each: list1.index(each) + list2.index(each) for each in list1 if each in list2}
        min_value = min(dic.values())
        result = [key for key, value in dic.iteritems() if value == min_value]
        return result
