class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)

        def dfs(step):
            if step >= len(cost):
                return 0
            if cache[step] != -1:
                return cache[step]

            currCost = cost[step] + min(dfs(step + 1), dfs(step + 2))

            cache[step] = currCost
            return currCost
        
        return min(dfs(0), dfs(1))