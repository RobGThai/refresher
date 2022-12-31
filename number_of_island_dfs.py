from typing import Tuple, Set
class Solution:
    """
    https://leetcode.com/problems/number-of-islands/description/
    DFS implementation
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0

        def dfs(grid: List[List[str]], row: int, col: int):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                """
                Out of bound
                """
                return
        
            if grid[row][col] != "1":
                """
                Not land
                """
                return

            grid[row][col] = "#" # Mark visited land
            l = dfs(grid, row, col - 1)
            u = dfs(grid, row - 1, col)
            r = dfs(grid, row, col + 1)
            d = dfs(grid, row + 1, col)

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == "1":
                    """
                    Look for a land then traverse the whole island and count them as 1
                    """
                    dfs(grid, row, col)
                    islandCount += 1

        return islandCount


