'''
Question:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example:
Input: [2,2,1]
Output: 1

Example:
Input: [4,1,2,1,2]
Output: 4

Author: https://github.com/ravikumark815
'''
import os
import sys

def singleNumber(nums) -> int:
    for i in nums:
        if (nums.count(i) == 1):
            return i

if __name__ == "__main__":
    liStr = input("\nProblem 1: Enter your list of integers separated by commas:")
    li = []
    li = liStr.split(",")
    print("Result:\t",singleNumber(li))