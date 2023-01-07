class Solution:
    """
    https://leetcode.com/problems/binary-search
    Simple binary search.
    """
    def search(self, nums: List[int], target: int) -> int:
        def divide(nums: List[int], start: int, end: int, target: int) -> int:
            mid_point = (end + start) // 2
            if nums[mid_point] == target:
                return mid_point
            
            if start == end:
                return -1

            return divide(nums, start, mid_point, target) if nums[mid_point] > target else divide(nums, mid_point + 1, end, target)
        return divide(nums, 0, len(nums) - 1, target)