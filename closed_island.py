from typing import List

class Solution:
    """
    https://leetcode.com/problems/number-of-closed-islands
    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        # for g in grid:
        #     print(g)

        max_width = len(grid[0])
        max_height = len(grid)
        closed_island = 0

        def probe_island(grid: List[List[int]], x: int, y: int, err: bool) -> int:
            if x < 0 or x >= max_width or y < 0 or y >= max_height:
                return 0
            
            if grid[y][x] > 0:
                return 1
            
            grid[y][x] = 2

            u = probe_island(grid, x - 1, y, err)
            d = probe_island(grid, x + 1, y, err)
            l = probe_island(grid, x, y - 1, err)
            r = probe_island(grid, x, y + 1, err)

            return u and d and l and r

        # Count the island
        for y in range(1, max_height - 1):
            for x in range(1, max_width - 1):
                if grid[y][x] == 0 and probe_island(grid, x, y, False):
                    closed_island += 1

        # print("End grid")
        # for g in grid:
        #     print(g)
        return closed_island