# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 592, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/problems/fraction-addition-and-subtraction/description/
''' 
# --------------------------------------------------- solution
'''
gcd
usage of Regex
'''
import re
class Solution(object):
    def upandlow(self, lis):
        up = []
        low = []
        for each in lis:
            if len(each) == 4:
                if each[0] == '-':
                    up.append(int(each[1])*-1)
                    low.append(int(each[3]))
                else:
                    up.append(int(each[1]))
                    low.append(int(each[3]))
            elif len(each) == 5:
                if each[1:3] == '10':
                    if each[0] == '-':
                        up.append(int(each[1:3])*-1)
                        low.append(int(each[4]))
                    else:
                        up.append(int(each[1:3]))
                        low.append(int(each[4]))
                else:
                    if each[0] == '-':
                        up.append(int(each[1])*-1)
                        low.append(int(each[3:5]))
                    else:
                        up.append(int(each[1]))
                        low.append(int(each[3:5]))
            else:
                if each[0] == '-':
                    up.append(-10)
                else:
                    up.append(10)
                low.append(10)
        return up, low
    
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        while b:
            a, b = b, a % b
        return a
        
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        expression = '+' + expression
        pattern = r'[+|-][0-9]+\/[0-9]+'
        m = re.findall(pattern, expression)
        uplis, lowlis = self.upandlow(m)
        templow = 1
        for each in lowlis:
            templow *= each
        mullis = [templow/low for low in lowlis]
        tempuplis = [a*b for a,b in zip(uplis,mullis)]
        tempup = sum(tempuplis)
        
        if tempup == 0:
            return "0/1"
        else:
            gcd_ = self.gcd(abs(tempup), templow)
            return "{}/{}".format(tempup/gcd_, templow/gcd_)
