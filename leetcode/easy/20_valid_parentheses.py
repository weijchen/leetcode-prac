# -*- coding: utf-8 -*-
'''
Link: https://leetcode.com/problems/valid-parentheses/
Tag: String, Stack
''' 
# --------------------------------------------------- solution
class Solution(object):
  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
      return True
    if len(s) == 1:
      return False
    if s[0] in [')', ']', '}']:
      return False
    paren_list = []
    ret = True
    for each in s:
      if each in ['(', '[', '{']:
        paren_list.append(each)
      else:
        if each == ')':
          if len(paren_list) == 0:
            return False
          comp = paren_list.pop(-1)
          if comp != '(':
            return False
        elif each == ']':
          if len(paren_list) == 0:
            return False
          comp = paren_list.pop(-1)
          if comp != '[':
            return False
        elif each == '}':
          if len(paren_list) == 0:
            return False
          comp = paren_list.pop(-1)
          if comp != '{':
            return False
    if len(paren_list) != 0:
      return False
    return ret
# --------------------------------------------------- best solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        for char in s:
            if char in "({[": left.append(char)
            elif char in ")}]":
                print(char)
                if left == []: return False
                if char == ')' and left[-1] != '(': return False
                if char == ']' and left[-1] != '[': return False
                if char == '}' and left[-1] != '{': return False
                left.pop()
        return left==[]