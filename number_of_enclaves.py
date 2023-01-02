from collections import deque
from typing import List

class Solution:
    """
    https://leetcode.com/problems/number-of-enclaves
    """

    def numEnclaves(self, grid: List[List[int]]) -> int:
        max_width = len(grid[0])
        max_height = len(grid)
        land_locked = 0
        visited = [[0 for w in range(max_width)] for h in range(max_height)]

        def dfs(q: deque):
            locked_found = 0
            
            while q:
                x, y = q.popleft()
                    
                if x < 0 or x >= max_width or y < 0 or y >= max_height:
                    "Exceed border"
                    continue
                
                if not grid[y][x]:
                    continue

                grid[y][x] = 0
                q.appendleft((x, y - 1))
                q.appendleft((x, y + 1))
                q.appendleft((x - 1, y))
                q.appendleft((x + 1, y))
        
        def bfs(q: deque):
            locked_found = 0
            
            while q:
                x, y = q.popleft()
                    
                if x < 0 or x >= max_width or y < 0 or y >= max_height:
                    "Exceed border"
                    continue
                
                if not grid[y][x]:
                    continue

                grid[y][x] = 0
                q.append((x, y - 1))
                q.append((x, y + 1))
                q.append((x - 1, y))
                q.append((x + 1, y))


        q = deque()
        for y in range(max_height):
            q.append((0, y))
            q.append((max_width - 1, y))
        
        for x in range(max_width):
            q.append((x, 0))
            q.append((x, max_height - 1))

        dfs(q)

        for g in grid:
            land_locked += sum(g)

        return land_locked