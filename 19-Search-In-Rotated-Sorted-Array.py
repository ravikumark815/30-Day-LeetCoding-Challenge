'''
Question:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Author: https://github.com/ravikumark815
'''

import os
import sys
import collections

def search(nums, target) -> int:
    if target in nums:
        return nums.index(target)
    return -1

if __name__ == "__main__":
    liStr = input("\nProblem 19: Enter your list of integers separated by commas:")
    target = input("Enter the target to search\t")
    li = liNum = []
    li = liStr.split(",")
    for i in li:
        liNum.append(int(i))
    print("Result:\t",search(liNum, target))