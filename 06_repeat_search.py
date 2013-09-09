#!/usr/bin/python
# Filename: 04_bst_compare.py
# Author  : Zhipeng JIANG
# Date    : Sep 7, 2013
# Question: http://www.careercup.com/question?id=21263687

def getDuplicatie(arr, size):
	i = 0
	for i in range(0, size):
		arr[arr[i%size]] += size
	for i in range(0, size):
		f = arr[i]/size;
		print 'Element =', i, 'frequency =', f


arr = [0, 1, 1]
getDuplicatie(arr, 3)
