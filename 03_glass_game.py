#!/usr/bin/python
# Filename: 03_glass_problem.py
# Author  : Zhipeng JIANG
# Date    : Sep 5, 2013

def setGlass(glasslist, pos, level, value):
	if value > 1:
		glasslist[pos] = 1
		value = (value - 1) / 2
		level += 1
		setGlass(glasslist, (pos+level), level, value)
		setGlass(glasslist, (pos+level+1), level, value)
	else:
		if pos in glasslist.keys():
			glasslist[pos] = glasslist[pos] + value
		else:
			glasslist[pos] = value
		
level = 0
glasslist = {}
litres = raw_input('Enter the litres of water:')
setGlass(glasslist, 0, 0, float(litres))
print 'Glasses are:\n', glasslist