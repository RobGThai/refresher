from typing import List

class Solution:
    """
    https://leetcode.com/problems/max-area-of-island
    """
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_width = len(grid[0])
        max_height = len(grid)
        largest_island = 0

        def probe_island(grid: List[List[int]], x: int, y: int) -> int:
            if x < 0 or x >= max_width or y < 0 or y >= max_height:
                return 0
            
            if grid[y][x] != 1:
                return 0
            
            grid[y][x] = 2 # Mark read; arbitrary number as we only focus for 1

            area = 1

            area += probe_island(grid, x - 1, y)
            area += probe_island(grid, x + 1, y)
            area += probe_island(grid, x, y - 1)
            area += probe_island(grid, x, y + 1)
            
            return area

        for y in range(0, max_height):
            for x in range(0, max_width):
                if grid[y][x] == 1:
                    "Calculate island size"
                    curr_size = probe_island(grid, x, y)
                    largest_island = max(largest_island, curr_size)
        
        return largest_island