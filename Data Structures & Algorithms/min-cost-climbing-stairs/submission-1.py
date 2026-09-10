class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Stores the length fo the costs array
        n = len(cost)

        # Stores the minimum cost that can be achieved at each step
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            # Stores the minimum possible cost that can be achieved at the current step
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # Returns the minimum calculated cost at the end of the array
        return dp[n]