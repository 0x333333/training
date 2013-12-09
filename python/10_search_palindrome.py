#!/usr/bin/python
# Filename: 09_search_sequence
# Author  : Zhipeng JIANG
# Date    : Sep 24, 2013

def longestPalSubStr(str, p):
	length = len(str)
	
	for i in range(0, length):
		i = length-1-i
		for j in range(0, i+1):
			if i == j:
				p[i][j] = True
			elif i+1 == j:
				p[i][j] = (str[i] == str[j])
			else:
				p[i][j] = (p[i+1][j-1]&(str[i]==str[j]))
			print p[i][j]

def longestPalSubStr(str):
	maxLength = 1
	start = 0
	length = len(str)
	low = -1
	low = -1
	for i in range(1, length):
		low = i-1
		high = i
		while low >= 0 && high < length && str[low] == str[high]:
			if high - low + 1 > maxLength:
				start = low
				maxLength = high - low + 1
			low = low - 1
			high = high + 1

		low = i-1
		high = i+1
		while low >= 0 && high < length && str[low] == str[high]:
			if high - low + 1 > maxLength:
				start = low
				maxLength = high - low + 1
			low = low - 1
			high = high + 1
	return maxLength


p = [[False, False, False],
	[False, False, False],
	[False, False, False]]
longestPalSubStr('aba', p)