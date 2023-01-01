class Solution:
    """
    https://leetcode.com/problems/climbing-stairs
    """
    def climbStairs(self, n: int) -> int:
        """ 
        Knowing 3 possible steps for 2-step ladder:
        1. 1 step + 1 step
        2. 2 steps
        Knowing 3 possible steps for 3-step ladder:
        1. 1 step + 1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step

        Step 4 example:
        - From 3 steps
        1. 1 step + 1 step + 1 step + 1 step
        2. 1 step + 2 steps + 1 step
        3. 2 steps + 1 step + 1 step

        - From 2 steps
        4. 1 step + 1 step + 2 step
        5. 2 steps + 2 step
        """
        steps = [1, 2, 3]


        for i in range(3, n):
            steps.append(steps[i - 1] + steps[i - 2])

        return steps[n - 1]