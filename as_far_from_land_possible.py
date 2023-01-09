from collections import deque
class Solution:
    """
    https://leetcode.com/problems/as-far-from-land-as-possible
    """
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        s = sum([sum(l) for l in grid])
        max_height = len(grid)
        max_width = len(grid[0])

        if s == 0 or s == max_height * max_width:
            return -1

        result = 0
        q = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for y in range(max_height):
            for x in range(max_width):
                if grid[y][x] == 1:
                    q.append((y, x))

        distance = 0
        while q:
            distance += 1

            for i in range(len(q)):
                y, x = q.popleft()
                for dy, dx in directions:
                    if dy + y >= max_height or dy + y < 0 or dx + x >= max_width or dx + x < 0 or grid[dy + y][dx + x] >= 1:
                        continue
                
                    grid[dy + y][dx + x] = distance
                    q.append((dy + y, dx + x))
            
            print(f"distance: {distance}")
            for y in range(max_height):
                print(grid[y])


        return distance - 1