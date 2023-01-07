from typing import List

class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        best_prices = 0

        for i, p in enumerate(prices):
            min_cost = min(min_cost, p)
            best_prices = max(best_prices, p - min_cost)


        return best_prices 