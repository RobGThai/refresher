class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        total = [0] * (max(nums) + 1)
        for n in nums:
            total[n] += n

        dp = [0] * len(total)
        dp[1] = total[1]

        for i in range(2, len(total)):
            dp[i] = max(dp[i - 1], dp[i - 2] + total[i])

        return dp[-1]
