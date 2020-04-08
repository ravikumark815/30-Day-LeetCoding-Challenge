'''
Question:
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

Note: The number of nodes in the given list will be between 1 and 100.

Author: https://github.com/ravikumark815
'''
import os
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self): 
        self.head = None

    def push(self, val):
        new_node = ListNode(val) 
        new_node.next = self.head 
        self.head = new_node

    def middleNode(self):
        cur = prev = self.head
        
        while (cur and cur.next):
            prev = prev.next
            cur = (cur.next).next
        print("The middle element is", prev.val)

if __name__ == "__main__":
    liStr = input("\nProblem 8: Enter your list of integers separated by commas:")
    li = liNum = []
    li = liStr.split(",")
    List_Node = LinkedList()
    for i in li:
        List_Node.push(int(i))
    List_Node.middleNode()