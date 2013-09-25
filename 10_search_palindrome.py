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

p = [[False, False, False],
	[False, False, False],
	[False, False, False]]
longestPalSubStr('aba', p)