from typing import List

class Solution:
    """
    https://leetcode.com/problems/house-robber/
    """
    def rob(self, nums: List[int]) -> int:
        """
        Same with steps-cost solution. Just different flavor

        Case skip one.
        2, 1, 1, 2 # Expect 4
        2, -, 1, -
        -, 1, -, 2
        2, -, -, 2
        
        2, 2, 3, 4
        """
        if len(nums) <= 2:
            return max(nums)

        accumulation = [0] * len(nums)
        accumulation[0] = nums[0]
        # As we can skip one. This will allow position 4 to pick the highest value between pos 0 and 1.
        accumulation[1] = max(nums[0], nums[1]) 


        for i in range(2, len(nums)):
            accumulation[i] = max(accumulation[i-1], accumulation[i-2] + nums[i])
            # accumulation[i] = max(accumulation[i-1], accumulation[i-2] + nums[i], accumulation[i - 3] + nums[i])

        return accumulation[-1]