class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        pac, atl = set(), set()

        def dfs(row, col, visit, lastHeight):
            if (row, col) in visit or row not in range(rows) or col not in range(cols) or heights[row][col] < lastHeight:
                return
            
            visit.add((row,col))

            for dr, dc in directions:
                nr,nc = dr + row, dc + col
                dfs(nr, nc, visit, heights[row][col])
            
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        result = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    result.append([i, j])
        
        return result
