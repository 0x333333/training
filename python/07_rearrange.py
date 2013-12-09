#!/usr/bin/python
# Filename: 04_bst_compare.py
# Author  : Zhipeng JIANG
# Date    : Sep 15, 2013
# Question: http://www.careercup.com/question?id=5700226908160000

def searchPos(list, num):
	for x in xrange(0, len(list)):
		if list[x] == num:
			return x
	return -1

def swap(list, p1, p2):
	tmp = list[p1]
	list[p1] = list[p2]
	list[p2] = tmp

# rawinput = raw_input('Enter the first list of numbers:')
# list1 = rawinput.split(' ')
# print list1
# rawinput = raw_input('Enter the second list of numbers:')
# list2 = rawinput.split(' ')
# print list2

list1 = [4, 0, 2, 1, 3]
print 'tgt:\n', list1
list2 = [3, 1, 0, 4, 2]
print 'src:\n', list2

pos = searchPos(list2, 0)
# swap(list2, 0, pos)

while list1[pos] != list2[pos]:
	pos2 = searchPos(list2, list1[pos])
	swap(list2, pos, pos2)
	print list2
	pos = pos2