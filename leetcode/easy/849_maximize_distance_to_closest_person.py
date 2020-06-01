# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 849, Created Jun. 2018
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/excel-sheet-column-number/description/
Tag: Array
''' 
# --------------------------------------------------- solution
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        anslis = []
        pair = []
        p1, p2 = 0, 0
        # add edge into the list
        seats = [2] + seats + [2]
        for idx, seat in enumerate(seats):
            if seat != 0:
                pair.append(idx)
            if len(pair) == 2:
                # has edge inside
                if seats[pair[0]] == 2 or seats[pair[1]] == 2:
                    temp_ans = int(pair[1] - pair[0]) -1
                    anslis.append(temp_ans)
                # no edge inside
                else:
                    temp_ans = int((pair[1] - pair[0])/2)
                    anslis.append(temp_ans)
                pair.pop(0)
            else:
                pass
        return max(anslis)
        