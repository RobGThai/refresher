class Solution:
    """
    https://leetcode.com/problems/n-th-tribonacci-number/description/
    Obvious solution is to use recursion but that would incur extra space complexity through memory stack. 
    Using list will require space complexity of O(n) and no call stack needed.
    """
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n == 2:
            return 1

        l = [0, 1, 1]

        for r in range(3, n + 1):
            l.append(l[r - 3] + l[r - 2] + l[r - 1])

        return l[n]
