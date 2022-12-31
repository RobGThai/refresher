class Solution:
    """
    https://leetcode.com/problems/running-sum-of-1d-array/description/
    """
    def runningSum(self, nums: List[int]) -> List[int]:
        result = nums[:1]

        for i in range(1, len(nums)):
            result.append(result[i - 1] + nums[i])
        
        return result