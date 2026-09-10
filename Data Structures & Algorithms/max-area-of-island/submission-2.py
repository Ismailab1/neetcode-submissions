class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0, -1]]

        def bfs(row, col):
            q = deque()
            grid[row][col] = 0
            q.append((row, col))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 0
                        res += 1
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea