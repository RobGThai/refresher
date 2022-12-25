import heapq
from typing import List

class Solution:
    """
    https://leetcode.com/problems/last-stone-weight/solutions/575336/official-solution/
    """
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x * -1, stones)) # Convert to max heap
        heapq.heapify(stones)
        size = len(stones)
        
        while len(stones) > 1:
            print(f"stones: {stones}")
            stone_x = heapq.heappop(stones)
            stone_y = heapq.heappop(stones)
            print(f"x[{stone_x}] y[{stone_y}]")

            smaller_stone = stone_x - stone_y
            if smaller_stone * -1 > 0:
                heapq.heappush(stones, smaller_stone)

        if len(stones) == 0:
            return 0
        
        return stones[0] * -1

class Case:
    def __init__(self, input: List[int], expect: int):
        self.input = input
        self.expect = expect

if __name__ == "__main__":
    test_cases = [
        Case([2,7,4,1,8,1], 1),
        Case([3,7,2], 2)
    ]

    for i, c in enumerate(test_cases):
        result = Solution().lastStoneWeight(c.input)
        print(f"Case[{i}] Result[{result == c.expect}] expect[{c.expect}] got[{result}]")