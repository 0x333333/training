#!/usr/bin/python
# Filename: ArrayList
# Author  : Zhipeng JIANG
# Date    : Sep 23, 2013

class ListNode:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class ArrayList:
	def __init__(self,size = 16):
        self.list = []
        self.size = size