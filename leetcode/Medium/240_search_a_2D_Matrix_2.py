# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 219, Created Oct. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/search-a-2d-matrix-ii/description/
Tag: Binary search, Divide and conquer
''' 
# --------------------------------------------------- solution
'''
Practice binary search
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if(self.binaryS(row, target)):
                return True
        return False
        
    def binaryS(self, arr, target):
        if len(arr) < 1:
            return False
        if len(arr) % 2 != 0:
            length = len(arr) - 1
        else:
            length = len(arr)
            
        if arr[length/2] == target:
            return True
        elif arr[length/2] > target:
            return self.binaryS(arr[:length/2], target)
        else:
            return self.binaryS(arr[(length/2)+1:], target)