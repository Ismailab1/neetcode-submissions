class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        seen = set()

        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or grid[row][col] == 0 or (row, col) in seen:
                return 0
            
            seen.add((row, col))
            
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        
        return maxArea
            