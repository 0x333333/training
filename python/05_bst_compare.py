#!/usr/bin/python
# Filename: 05_bst_compare.py
# Author  : Zhipeng JIANG
# Date    : Sep 7, 2013
# Question: http://www.careercup.com/question?id=19016700


# compare two lists
def compare(list1, list2):
	length1 = len(list1)
	length2	= len(list2)
	if length1 != length2:
		return False
	if list1[0] != list2[0]:
		return False

	list1_greater = []
	list2_greater = []
	list1_less = []
	list2_less = []

	for i in range(1, length1):
		if list1[i] > list1[0]:
			list1_greater.append(list1[i])
		elif list1[i] < list1[0]:
			list1_less.append(list1[i])
		else:
			return False
	
		if list2[i] > list2[0]:
			list2_greater.append(list2[i])
		elif list2[i] < list2[0]:
			list2_less.append(list2[i])
		else:
			return False

	return checkEqual(list1_greater, list2_greater) and checkEqual(list1_less, list2_less)

# check the two lists are equal or not
def checkEqual(List1, List2):
	if len(List1) != len(List2):
		return False
	for i in range(0, len(List1)):
		if List1[i] != List2[i]:
			return False

	return True



rawinput = raw_input('Enter the first list of numbers:')
list1 = rawinput.split(' ')
rawinput = raw_input('Enter the second list of numbers:')
list2 = rawinput.split(' ')
print compare(list1, list2)