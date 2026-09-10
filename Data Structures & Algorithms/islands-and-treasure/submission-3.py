class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inf = 2147483647

        def bfs(row, col):
            q = deque([(row, col)])
            visit = [[False] * cols for _ in range(rows)]
            visit[row][col] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if grid[r][c] == 0:
                        return steps
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and not visit[nr][nc] and grid[nr][nc] != -1):
                            visit[nr][nc] = True # Mark the neighbor, not the parent
                            q.append((nr, nc))
                steps += 1
            return inf


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == inf:
                    grid[i][j] = bfs(i, j)
        