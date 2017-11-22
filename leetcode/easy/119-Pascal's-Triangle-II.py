# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 119, Created Nov. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/pascals-triangle-ii/description/
Tag: Array
''' 
# --------------------------------------------------- solution
'''
Combine two arrays, both miss one element
while loop for recording pascals layer
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = 0
        arr = [1]
        while row < rowIndex:
            temparr_1 = arr+[0]
            temparr_2 = [0]+arr
            for each in range(len(temparr_1)):
                temparr_1[each] += temparr_2[each]
            arr = temparr_1
            row += 1
        return arr

# --------------------------------------------------- better solution
'''
Use zip() function to concate two arrays
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = 0
        arr = [1]
        while row < rowIndex:
            arr = [x + y for x, y in zip(arr+[0], [0]+arr)]
            row += 1
        return arr