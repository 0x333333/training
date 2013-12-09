#!/usr/bin/python
# Filename: 09_search_sequence
# Author  : Zhipeng JIANG
# Date    : Sep 24, 2013
# Question: http://www.careercup.com/question?id=11070934

def find(arr):
    table = {}
    first = 0
    last = 0
    for i in arr:
        beg = end = i
        if i in table:
            continue
        
        table[i] = 'EXISTED'
        if i - 1 in table:
            beg = table[i-1]
        if i + 1 in table:
            end = table[i+1]
        
        table[beg] = end
        table[end] = beg
        
        if end - beg > last - first:
            first = beg
            last = end
        print 'i: ', i
        print 'table: ', table
        print 'first: ', first, ' last: ', last
        print '------'
    return list(range(first, last + 1))

arr = [3, 6, 10, 4, 7, 9, 1, 8, 11]
# print arr
# print '------'
print(find(arr))