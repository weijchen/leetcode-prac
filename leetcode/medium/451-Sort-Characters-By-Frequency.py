# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 451, Created Nov. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/sort-characters-by-frequency/description/
Tag: Hash Table, Heap
''' 
# --------------------------------------------------- solution
'''
1. Use set() to find all variable.
2. Find correct position for each frequency pair, then insert into array. (Build heap structure)
3. Return answer in request format.
'''
class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for each in set(s):
            c = s.count(each)
            if len(arr) == 0:
                arr.append([each, c])
            else:
                id_ = 0
                for idx in range(len(arr)):
                    if arr[idx][1] >= c:
                        id_ += 1
                arr.insert(id_, [each, c])
        
        strans = ''
        for each in arr:
            strans += each[0]*each[1]
        return strans

