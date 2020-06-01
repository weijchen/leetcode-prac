# -*- coding: utf-8 -*-
'''
Link: https://leetcode.com/problems/palindrome-number/description/
Tag: Math
''' 
# --------------------------------------------------- solution 1
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x % 10 == 0 and x != 0 or x < 0:
            return False
        if 0 <= x <= 9:
            return True
        reverted = 0
        while x > 0:
            reverted *= 10
            reverted += x % 10
            if reverted == x:
                return True
            else:
                x /= 10
                if reverted == x:
                    return True
        return False

# ---------------------------------------------------- solution 2
class Solution(object):
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if x < 0:
		  return False
		else
			if x == int(str(x)[::-1]):
				return True
			else:
				return False
