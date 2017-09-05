# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 476, Created Aug. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/number-complement/description/
''' 
# --------------------------------------------------- solution
import math

class Solution(object):
    def findComplement(num):
        """
        :type num: int
        :rtype: int
        """
        # decimal to binary
        lis = []
        while num / 2 != 0:
            lis.append(num % 2)
            num = math.floor(num/2)
        newlis = []

        # trans complement
        for i in reversed(lis):
            if i == 0:
                newlis.append(1)
            elif i == 1:
                newlis.append(0)

        # binary to decimal
        answer = 0
        for char in range(len(newlis)):
            answer += newlis[char]*2**(len(newlis)-1-char)
        return answer
r = Solution.findComplement(5)
print(r)
# # -- best solution --
# class Solution(object):
#     def findComplement(num):
#         i = 1
#         while i <= num:
#             # print(i)
#             i <<= 1
#             print(i)
#             print(i^num)
#             # print((i-1)^num)
#         return (i - 1) ^ num

# r = Solution.findComplement(5)
# print(r)