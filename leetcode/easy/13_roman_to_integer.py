# -*- coding: utf-8 -*-
'''
Link: https://leetcode.com/problems/roman-to-integer/
Tag: Math, String
''' 
# --------------------------------------------------- solution
class Solution(object):
  def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    char_list = [_ for _ in s]
    total = 0
    temp_str = None
    for each in char_list:
      if each == 'I':
        total += 1
      elif each == 'V':
        if temp_str == 'I':
          total -= 2
        total += 5
      elif each == 'X':
        if temp_str == 'I':
          total -= 2
        total += 10
      elif each == 'L':
        if temp_str == 'X':
          total -= 20
        total += 50
      elif each == 'C':
        if temp_str == 'X':
          total -= 20
        total += 100
      elif each == 'D':
        if temp_str == 'C':
          total -= 200
        total += 500
      elif each == 'M':
        if temp_str == 'C':
          total -= 200
        total += 1000
      temp_str = each
    return total
# --------------------------------------------------- alternative solution
class Solution(object):
  def romanToInt(self, s):
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
    number = 0
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    for char in s:
      number += translations[char]
    return number