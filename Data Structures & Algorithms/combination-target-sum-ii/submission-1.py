class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return
            for pos in range(i, len(candidates)):
                if pos > i and candidates[pos] == candidates[pos - 1]:
                    continue
                curr.append(candidates[pos])
                dfs(pos + 1, curr, total + candidates[pos])
                curr.pop()
            
        
        dfs(0, [], 0)

        return res