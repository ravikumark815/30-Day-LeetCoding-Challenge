'''
Question:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Author: https://github.com/ravikumark815
'''
import os
import sys

def moveZeroes(nums):
    c = 0
    n = len(nums)
    i = 0
    while i<n:
        if nums[i]==0:
            c = c+1
            del nums[i]
            n = n-1
            i = i-1
        i = i+1
    while c != 0:
        nums.append(0)
        c = c-1
    return nums

if __name__ == "__main__":
    liStr = input("\nProblem 5: Enter your list of integers separated by commas:")
    li = liNum = []
    li = liStr.split(",")
    for i in li:
        liNum.append(int(i))
    print("Result:\t",moveZeroes(liNum))