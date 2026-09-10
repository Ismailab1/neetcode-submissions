class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        time = 0
        fresh = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))
                
            time += 1
        
        return time if fresh == 0 else -1