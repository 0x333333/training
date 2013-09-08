#!/usr/bin/python
# Filename: 04_glass_problem.py
# Author  : Zhipeng JIANG
# Date    : Sep 5, 2013

# You are given an integer array, 
# where all numbers except for TWO numbers appear even number of times. 
# Q: Find out the two numbers which appear odd number of times.

list = [100, 22, 100, 22]
res = 0
for x in xrange(0, 4):
	res ^= list[x]
	print res

print 1^3
