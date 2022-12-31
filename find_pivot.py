class Solution:
    """
    https://leetcode.com/problems/find-pivot-index/description/
    """
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)

        for i, n in enumerate(nums):
            left += n

            if left == right:
                return i

            right -= n
        return -1