class Solution:
    """
    https://leetcode.com/problems/is-subsequence/
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        p = 0
        for i in range(len(t)):
            if t[i] == s[p]:
                p += 1
            if p == len(s):
                break
        
        return p == len(s)