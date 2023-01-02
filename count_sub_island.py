from collections import deque
from typing import List

class Solution:
    """
    https://leetcode.com/problems/count-sub-islands
    """
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        max_height = len(grid2)
        max_width = len(grid2[0])
        sub_islands = 0

        def bfs(q: deque) -> bool:
            result = True
            while q:
                x, y = q.popleft()
                if x < 0 or x >= max_width or y < 0 or y >= max_height:
                    # Guard OOB
                    continue

                if grid2[y][x] == 0:
                    continue

                grid2[y][x] = 0 # Fill this to not repeat work

                if grid1[y][x] == 0:
                    # This island is not a subset of grid1
                    result = False
                
                q.append((x - 1, y))
                q.append((x + 1, y))
                q.append((x, y - 1))
                q.append((x, y + 1))

            return result

        q = deque()
        for y in range(max_height):
            for x in range(max_width):
                if grid2[y][x] == 1:
                    q.append((x, y))
                    sub_islands += 1 if bfs(q) else 0

        return sub_islands