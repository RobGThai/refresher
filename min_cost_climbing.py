from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        accumulation = cost[:2]

        for i in range(2, len(cost)):
            accumulation.append(min(accumulation[i - 1], accumulation[i - 2]) + cost[i])

        print(f"acc: {accumulation}")
        return min(accumulation[-1], accumulation[-2])