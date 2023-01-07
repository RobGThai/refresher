# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    """
    https://leetcode.com/problems/first-bad-version
    Divide and conquer using two pointers.
    """
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1

        start = 0
        end = n

        while start <= n:
            mid = (start + end) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                else: 
                    end = mid
            else:
                start = mid + 1