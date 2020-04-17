'''
Question:
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
- An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].

Author: https://github.com/ravikumark815
'''

import os
import sys

def checkValidString(s):
    leftBalance = rightBalance = 0
    n = len(s)
    for i in range(n):
        if s[i] in "(*":
            leftBalance += 1
        else:
            leftBalance -= 1
        if s[n-i-1] in "*)":
            rightBalance += 1
        else:
            rightBalance -= 1
        if leftBalance < 0  or rightBalance < 0:
            return False
    return True

if __name__ == "__main__":
    string = input("\nProblem 16: Enter the string to validate its paranthesis:")
    print("Result:\t", checkValidString(string))