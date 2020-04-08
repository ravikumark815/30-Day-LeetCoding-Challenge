'''
Question:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Author: https://github.com/ravikumark815
'''
import os
import sys

def maxSubArray(nums):
        subArraySum = nums[0]
        resSum = nums[0]

        for i in range(1,len(nums)):
            subArraySum = max(subArraySum+nums[i], nums[i])
            resSum = max(subArraySum, resSum)
        return resSum

if __name__ == "__main__":
    liStr = input("\nProblem 5: Enter your list of integers separated by commas:")
    li = liNum = []
    li = liStr.split(",")
    for i in li:
        liNum.append(int(i))
    print("Result:\t",maxSubArray(liNum))