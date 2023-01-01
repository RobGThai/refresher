class Solution: 
    """
    https://leetcode.com/problems/isomorphic-strings
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        max_length = len(s)
        change_map = {}
        change_set = set()
        
        for i in range(max_length):
            if s[i] in change_map:
                if change_map[s[i]] != t[i]:
                    # Previously replaced character doesn't match the one we need at this position.
                    return False
            elif t[i] in change_set:
                # The target character was used on a different source.
                return False
            else:
                # Record replacement for lookup
                change_map[s[i]] = t[i]
                change_set.add(t[i])

        return True