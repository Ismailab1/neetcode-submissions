class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(pos, curr):
            res.append(curr.copy())

            if pos >= len(nums):
                return

            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])

        return res