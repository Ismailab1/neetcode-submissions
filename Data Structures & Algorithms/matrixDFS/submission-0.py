class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # Step 1: Initialize the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])  # Get the number of rows and columns
        
        # Step 2: Define the helper function for recursive depth-first search (DFS)
        def helper(grid: List[List[int]], r: int, c: int, visit: set) -> int:
            # Base case: if the current cell is out of bounds, a wall, or already visited, return 0
            if (min(r, c) < 0 or  # If either row or column index is negative (out of bounds)
                r == ROWS or  # If the row index exceeds the grid bounds
                c == COLS or  # If the column index exceeds the grid bounds
                (r, c) in visit or  # If the cell has already been visited in the current path
                grid[r][c] == 1):  # If the cell is a wall (1 means obstacle)
                return 0
            
            # Base case: if we've reached the bottom-right corner (destination), return 1
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            # Mark the current cell as visited
            visit.add((r, c))
        
            # Initialize count of paths from the current cell
            count = 0
            
            # Step 3: Recursively explore all 4 possible directions (down, up, right, left)
            count += helper(grid, r + 1, c, visit)  # Move down
            count += helper(grid, r - 1, c, visit)  # Move up
            count += helper(grid, r, c + 1, visit)  # Move right
            count += helper(grid, r, c - 1, visit)  # Move left

            # Step 4: Backtrack by removing the current cell from the visited set
            visit.remove((r, c))
            
            # Return the total count of valid paths from the current cell
            return count
    
        # Step 5: Call the helper function starting from the top-left corner (0, 0) with an empty visited set
        return helper(grid, 0, 0, set())
