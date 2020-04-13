'''
Question:
We have a collection of stones, each stone has a positive integer weight.
Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
 

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000

Author: https://github.com/ravikumark815
'''

import os
import sys

def findMaxLength(nums):
        a = 0
        li_dict = {0: -1}
        max_length = 0
        
        for k, v in enumerate(nums):
            if v == 1:
                a += 1
            else:
                a -= 1
            if a in li_dict:
                length = k - li_dict[a]
                max_length = max(max_length, length)
            else:
                li_dict[a] = k
        return max_length

if __name__ == "__main__":
    liStr = input("\nProblem 13: Enter your list of integers separated by commas:")
    li = liNum = []
    li = liStr.split(",")
    for i in li:
        liNum.append(int(i))
    print("Result:\t", findMaxLength(liNum))