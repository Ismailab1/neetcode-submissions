class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[1,0], [-1, 0], [0,1],[0,-1]]
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        cells = []

        def dfs(row, col, visit, prevHeight):
            if ((row, col) in visit or row < 0 or row == ROWS or col < 0 or col == COLS or heights[row][col] < prevHeight):
                return

            visit.add((row, col))

            for dr, dc in directions:
                dfs(row + dr, col + dc, visit, heights[row][col])
            
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    cells.append((r,c))
        return cells