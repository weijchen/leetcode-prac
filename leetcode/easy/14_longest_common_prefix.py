# -*- coding: utf-8 -*-
'''
Link: https://leetcode.com/problems/roman-to-integer/
Tag: Math, String
''' 
# --------------------------------------------------- solution
class Solution(object):
  def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    checker = len(set(strs))
    if checker > 1:
      # minlen = min([len(each) for each in strs])
      minlen = len(min(strs, key=len))  # find the element with shortest length, then calculate its length
      ret = ""
      end = False
      for l in range(minlen):
        comp_set = list(set([each[:minlen][l] for each in strs]))
        if len(comp_set) == 1:
          ret += comp_set[0]
        else:
          return ret
      return ret
    elif checker == 1:
      return strs[0]
    else:
      return ""