class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        seen = set()

        def dfs(row, col, currArea):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1 or (row, col) in seen:
                return currArea

            currArea += 1
            seen.add((row, col))

            for dr, dc in directions:
                currArea = max(currArea, dfs(row + dr, col + dc, currArea))

            return currArea

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j, 0))

        return maxArea

