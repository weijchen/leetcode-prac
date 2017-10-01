# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: insertion sort, Created Jul. 2017
Ver: 1.0 (finish)
Link: 
''' 
# --------------------------------------------------- libs import
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            temp = key
            l[j+1] = l[j]
            l[j] = temp
            j -= 1

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))