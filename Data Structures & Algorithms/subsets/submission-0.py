class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        sub = []

        def dfs(arr, i):
            if i == len(nums):
                subsets.append(sub.copy())
                return 
            
            sub.append(nums[i])
            dfs(sub, i + 1)
            
            sub.pop()
            dfs(sub, i + 1)

        dfs(sub, 0)

        return subsets