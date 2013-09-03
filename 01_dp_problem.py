#!/usr/bin/python
# Filename: 01_dp_problem.py
# Author  : Zhipeng JIANG
# Date    : Sep 4, 2013

####################
# function
####################
def MaxAdjVal(values, length):
	Sum = 0
	Max = int(values[0])
	for i in range(0, length):
		# print values[i]
		Sum += int(values[i])
		if Sum > Max:
			Max = Sum
		if Sum < 0:
			Sum = 0
	return Max

####################
# body
####################
strings = '5 6 -1 5 4 -7'
values = strings.split(' ')
print 'values:', values
res = MaxAdjVal(values, len(values))
print 'res is', res

strings = '7 0 6 -1 1 -6 7 -5'
values = strings.split(' ')
print 'values:', values
res = MaxAdjVal(values, len(values))
print 'res is', res