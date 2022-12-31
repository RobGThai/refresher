from collections import deque
class Solution:
    """
    https://leetcode.com/problems/flood-fill/description/
    Further optimization can be done by keeping track of visited pixel and exclude them from the queue.
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append((sr, sc))
        target = image[sr][sc]

        if target == color:
            return image

        while len(q) > 0:
            row, col = q.popleft()
            image[row][col] = color
            if row > 0 and image[row - 1][col] == target:
                q.append((row - 1, col))
            if row < len(image) - 1 and image[row + 1][col] == target:
                q.append((row + 1, col))
            if col > 0 and image[row][col - 1] == target:
                q.append((row, col - 1))
            if col < len(image[0]) - 1 and image[row][col + 1] == target:
                q.append((row, col + 1))
        
        return image