class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Stores the min cost of each step
        memo = [-1] * len(cost)

        
        def dfs(i):
            # If we pass the last step
            if i >= len(cost):
                return 0
            # If the current step has been accounted for
            if memo[i] != -1:
                return memo[i]

            # Stores the minimum of either going forward one step or two steps
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return memo[i]
            
        # Returns the minimum of either starting from the 0th step or the 1st step
        return min(dfs(0), dfs(1))