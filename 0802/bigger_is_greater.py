# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: bigger is greater, Created Jul. 2017
Ver: 1.0 (sample test done, failed on sumbit test)
Link: https://www.hackerrank.com/challenges/bigger-is-greater?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
''' 
# --------------------------------------------------- libs import
import sys

def big_is_great(w):
	wordlis = []
	for i in w:
		wordlis.append(i)
	for i in range(len(w)-1, 0, -1):
		if wordlis[i] > wordlis[i-1]:

			wordlis[i], wordlis[i-1] = wordlis[i-1], wordlis[i]
			wordlis = ''.join(wordlis)
			return wordlis
		else:
			target = wordlis[0]
			wordlis = sorted(wordlis)
			check = ''.join(wordlis)
			for i in range(len(wordlis)):
				if wordlis[i] == target:
					idx = i+1
					new_head = wordlis[idx]
					wordlis.pop(idx)
					wordlis = new_head + ''.join(wordlis)
					if wordlis == check:
						return 'no answer'
					else:
						return wordlis
for _ in range(int(input())):
	w = input()
	print(big_is_great(w))

# -- Solution --
for _ in range(int(input())):
    s = input()
    has_greater = False
    for i in range(len(s)-1)[::-1]:
        if ord(s[i]) < ord(s[i+1]):
            for j in range(i+1,len(s))[::-1]:
                if ord(s[i]) < ord(s[j]):
                    lis = list(s)
                    lis[i],lis[j]=lis[j],lis[i]
                    print("".join(lis[:i+1]+lis[i+1:][::-1]))
                    has_greater = True
                if has_greater == True:
                    break
        if has_greater == True:
            break
    if has_greater == False:
        print("no answer")