class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0),(0,1),(0,-1)]
        seen = set()

        def dfs(row, col):
            if grid[row][col] == "0":
                return
            
            seen.add((row,col))

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen:
                    dfs(nr, nc)
        
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    islands += 1
                    dfs(i, j)
        
        return islands
