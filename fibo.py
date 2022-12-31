class Solution:
    """
    https://leetcode.com/problems/fibonacci-number/description/
    """
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        l = [0, 1]
        for r in range(2, n + 1):
            l.append(l[r - 1] + l[r - 2])

        return l[n]