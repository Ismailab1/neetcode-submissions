class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # Sets the directions of the BFS
        ROWS, COLS = len(grid), len(grid[0]) # Sets the bounds
        islands = 0

        def bfs(r,c):
            q = deque() # Starts a queue for each node
            grid[r][c] = "0" # Sets the current node to "0"

            q.append((r,c)) # Appends the current node to the queue

            while q: # While there are still nodes (lands) to traverse
                row, col = q.popleft() # Pops the top node
                for dr, dc in directions:
                    nr, nc = dr + row,  dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc)) # If there is a new land in a new direction, append that land to the queue
                    grid[nr][nc] = "0"
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        return islands