class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0]) # Gives the bounds for the matrix
        directions = [[0,1], [0,-1],[1,0],[-1,0]] # Sets the directions for our search
        islands = 0 # Tracks the number of islands

        # Our main traversal method
        def dfs(row, col):

            # Checks if our current position is on an edge or not
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0"):
                return
            
            # Sets the current position to "0", to ensure we don't count the current land again
            grid[row][col] = "0"

            # Recursively checks the surrounding positions by using the directions array
            for dr, dc in directions:
                dfs(row + dr, col + dc)
            
        # One-pass through the array to check for any untracked islands
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        # Returns the number of islands
        return islands


