from collections import Counter

class Solution:
    """
    https://leetcode.com/problems/longest-palindrome/
    """
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        if len(s) == 1:
            return 1
        counter = Counter(s)
        has_single = False
        for c in counter:
            if counter[c] % 2 != 0:
                has_single = True
                longest += counter[c] - 1
            else:
                longest += counter[c]

        if has_single:
            longest += 1

        return longest