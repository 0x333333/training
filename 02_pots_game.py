#!/usr/bin/python
# Filename: 02_pots_game.py
# Author  : Zhipeng JIANG
# Date    : Sep 4, 2013
# Question: http://jesusjzp.github.io/blog/2013/09/04/algorithm-training-pots-game/

def max_coin(pots, start, end):
	if start > end:
		return 0

	a = pots[start] + min(max_coin(pots, start+2, end), max_coin(pots, start+1, end-1))
	b = pots[end] + min(max_coin(pots, start+1, end-1), max_coin(pots, start, end-2))

	return max(a, b)



pots = [3, 4, 7, 5]
print "The max coins are", max_coin(pots, 0, 3)