class Solution:
    def climbStairs(self, n: int) -> int:
        # Returns the num of ways of the nth stair
        if n <= 2:
            return n
        
        # Dp array for storing the ways a current step can be traversed
        dp = [0] * (n + 1)

        # Storing the first two steps to iterate from
        dp[1] = 1
        dp[2] = 2

        # Traverse through the steps
        for i in range(3, n + 1):
            # Takes the num of ways stortes at the last two step and adds them to the ith step
            dp[i] = dp[i - 1] + dp[i - 2]
        
        # Returns the num of ways to get to teh nth step after iterating through eachs tep
        return dp[n]