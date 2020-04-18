'''
Question:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011

Output: 3

Author: https://github.com/ravikumark815
'''

import os
import sys
import collections

def numIslands(grid):
    try: 
        m,n = len(grid), len(grid[0])
    except: 
        return 0
    cnt = 0
    ones = { (i,j) for i in range(m) for j in range(n) if grid[i][j]=="1" }
    while ones:
        queue = collections.deque([ ones.pop() ])
        while queue:
            i,j = queue.popleft()   # BFS
            # i,j = queue.pop()       # DFS
            for x,y in (i+1,j), (i-1,j), (i,j+1), (i,j-1):
                if 0<=x<m and 0<=y<n and (x,y) in ones:
                    ones.discard( (x,y) )
                    queue.append( (x,y) )
        cnt += 1
    return cnt

if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print("Result:\t", numIslands(grid))