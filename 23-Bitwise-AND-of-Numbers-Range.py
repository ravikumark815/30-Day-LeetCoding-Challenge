'''
Question:
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0

Author: https://github.com/ravikumark815
'''

import os
import sys
import collections

def rangeBitwiseAnd(m,n):
    if (m==0) or (n==0) or (n >= (m*2)):
        return 0
    i = m+1
    res = m
    while (i<=n):
        res = res & i
        i = i+1
    return res

if __name__ == "__main__":
    m = int(input("Enter m value:\t"))
    n = int(input("Enter n value:\t"))
    print("Result:\t", rangeBitwiseAnd(m,n))