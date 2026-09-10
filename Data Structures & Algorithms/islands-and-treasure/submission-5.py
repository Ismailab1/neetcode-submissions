class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        inf = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            r, c = q.popleft()
                    
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr in range(rows) and nc in range(cols) and grid[nr][nc] == inf:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
