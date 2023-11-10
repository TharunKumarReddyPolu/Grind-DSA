'''
Problem Statement: https://leetcode.com/problems/number-of-islands/

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

'''

from typing import List, Optional
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            visited.add((r, c))
            q.append((r,c))

            while q:
                row, col = q.popleft() # change popleft() to pop() -> DFS iterative
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and c in range(COLS) and 
                        grid[r][c] == '1' and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands