'''
Question:
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
- 1 <= S.length <= 200
- 1 <= T.length <= 200
- S and T only contain lowercase letters and '#' characters.

Author: https://github.com/ravikumark815
'''
import os
import sys

def backspaceCompare(S,T) -> int:
    s = ""
    t = ""
    
    for c in S:
        if c == "#":
            s = s[:-1]
        else:
            s += c
    
    for c in T:
        if c == "#":
            t = t[:-1]
        else:
            t += c
    
    return s == t

if __name__ == "__main__":
    S = input("\nProblem 9\nS: ")
    T = input("T: ")
    print("Result:\t",backspaceCompare(S,T))