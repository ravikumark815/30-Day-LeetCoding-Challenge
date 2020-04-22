'''
Question:
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.

Author: https://github.com/ravikumark815
'''

import os
import sys
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    i = 1
    while i<len(preorder) and preorder[i]<root.val:
        i+=1
    root.left = bstFromPreorder(preorder[1:i])
    root.right = bstFromPreorder(preorder[i:])
    return root

if __name__ == "__main__":
    liStr = input("\nProblem 5: Enter your list of integers separated by commas that represent the preorder traversal:")
    li = liNum = []
    li = liStr.split(",")
    for i in li:
        liNum.append(int(i))
    print("Result:\t",bstFromPreorder(liNum))