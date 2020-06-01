# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 447, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/number-of-boomerangs/description/
Tag: Hash Table
''' 
# --------------------------------------------------- solution
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
                for p in points:
                    cmap = {}
                    for q in points:
                        f = p[0]-q[0]
                        s = p[1]-q[1]
                        cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
                    for k in cmap:
                        res += cmap[k] * (cmap[k] -1)
                return res