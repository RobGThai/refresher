from typing import List

class Solution:
    """
    https://leetcode.com/problems/house-robber-ii
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        d1 = [0] * len(nums)
        d1[0] = nums[0]
        d1[1] = max(nums[0], nums[1])

        d2 = [0] * len(nums)
        d2[0] = 0
        d2[1] = nums[1]

        for i in range(2, len(nums) - 1):
            d1[i] = max(d1[i-1], d1[i-2] + nums[i])
            d2[i] = max(d2[i-1], d2[i-2] + nums[i])
        last_pos = len(nums) - 1
        d2[last_pos] = max(d2[last_pos-1], d2[last_pos-2] + nums[last_pos])

        return max(d2[-1], d1[-1], d1[-2])