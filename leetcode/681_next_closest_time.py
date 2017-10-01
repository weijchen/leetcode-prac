# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: leetcode 681, Created Sep. 2017
Ver: 1.0 (finish)
Link: https://leetcode.com/contest/leetcode-weekly-contest-51/problems/next-closest-time/
''' 
# --------------------------------------------------- solution
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        strlis = [int(each) for each in time if each != ':']
        compare = strlis[0]*1000 + strlis[1]*100 + strlis[2]*10 + strlis[3]
        anslis = []
        for each1 in strlis:
            for each2 in strlis:
                for each3 in strlis:
                    for each4 in strlis:
                        anslis.append((each1, each2, each3, each4))
        ph2 = []
        for each in anslis:
            timelis = [element for element in each]
            timenum = int(each[0])*1000 + int(each[1])*100 + int(each[2])*10 + int(each[3])
            if timenum <= 2400 and timenum > compare:
                if int(timelis[2]) < 6:
                    ph2.append(timenum)
        
        if len(ph2) == 0:
            return str(min(strlis))*2 + ':' + str(min(strlis))*2
        ans = min(ph2)
        anslis = list(str(ans))
        if len(anslis) == 3:
            return '0' + str(anslis[0]) + ':' + str(anslis[1]) + str(anslis[2]) 
        elif len(anslis) == 2:
            return '0' + '0' + ':' + str(anslis[0]) + str(anslis[1])
        elif len(anslis) == 1:
            return '0' + '0' + ':' +'0' + str(anslis[0])
        else:
            return str(anslis[0]) + str(anslis[1]) + ':' + str(anslis[2]) + str(anslis[3])     