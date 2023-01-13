class Solution:
    """
    https://leetcode.com/problems/remove-duplicates-from-sorted-array
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] <= curr:
                nums.pop(i)
            else:
                curr = nums[i]
                i += 1

        return i