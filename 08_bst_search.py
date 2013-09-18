#!/usr/bin/python
# Filename: 08_bst_search.py
# Author  : Zhipeng JIANG
# Date    : Sep 18, 2013
# Question: http://www.careercup.com/question?id=15320677

from Queue import Queue

class BinaryTreeNode:
    def __init__(self,data,left,right):
        self.left = left
        self.data = data
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
    def makeTree(self,data,left,right):
        self.root = BinaryTreeNode(data,left,right)
        #left.root = right.root = None
    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False
    def preOrder(self,r):
        if r.root is not None:
            print(r.root.data)
            if r.root.left is not None:
                self.preOrder(r.root.left)
            if r.root.right is not None:
                self.preOrder(r.root.right)
    def inOrder(self,r):
        if r.root is not None:
            if r.root.left is not None:
                self.inOrder(r.root.left)
            print(r.root.data)
            if r.root.right is not None:
                self.inOrder(r.root.right)
    def postOrder(self,r):
        if r.root is not None:
            if r.root.left is not None:
                self.preOrder(r.root.left)
            if r.root.right is not None:
                self.preOrder(r.root.right)
            print(r.root.data)
    def levelOrder(self,a):
        q = Queue()
        r = a
        while r is not None:
            print(r.root.data)
            if r.root.left is not None:
                q.add(r.root.left)
            if r.root.right is not None:
                q.add(r.root.right)
            if q.isEmpty():
                print("empty")
                r = None
            else:
                r = q.delete()
            


r = BinaryTree()
ra = BinaryTree()
ra.makeTree(2,None,None)
rb = BinaryTree()
rb.makeTree(3,None,None)
r.makeTree(1,ra,rb)
print("preOrder")
r.preOrder(r)
print("inOrder")
r.inOrder(r)
print("postOrder")
r.postOrder(r)
print("levelOrder")
r.levelOrder(r)