'''
Question:
Given an array of strings, group anagrams together.

Example:
Input: ["eat","tea","tan","ate","nat","bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
- All inputs will be in lowercase.
- The order of your output does not matter.

Author: https://github.com/ravikumark815
'''
import os
import sys

def groupAnagrams(strs):
    res = []
    d = {("".join(sorted(i))):[] for i in strs}
    for i in strs:
        d["".join(sorted(i))].append(i)
    for k in d:
        res.append(d[k])
    return res

if __name__ == "__main__":
    liStr = input("\nProblem 5: Enter your list of strings separated by commas:")
    li = liNum = []
    li = liStr.split(",")
    print("Result:\t",groupAnagrams(li))