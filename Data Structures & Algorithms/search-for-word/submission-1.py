class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        rows, cols = len(board), len(board[0])
        
        # A set to keep track of visited cells in the current path
        # This prevents using the same letter twice in one path
        path = set()

        def dfs(r, c, i):
            """
            Depth-First Search function.
            r: current row
            c: current col
            i: current index in the word we are searching for
            """
            # 1. Base Case: Success
            # If we have found all characters in the word
            if i == len(word):
                return True

            # 2. Base Cases: Failure conditions for the current path
            if (r < 0 or c < 0 or                   # Out of bounds (top/left)
                r >= rows or c >= cols or           # Out of bounds (bottom/right)
                word[i] != board[r][c] or           # Character doesn't match
                (r, c) in path):                    # Cell has already been visited in this path
                return False

            # 3. Recursive Step
            # Add the current cell to the path (mark as visited for this path)
            path.add((r, c))

            # Explore all 4 directions (up, down, left, right)
            # We are looking for the next character (i + 1)
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # 4. Backtrack
            # Remove the cell from the path, so it can be used in other paths
            path.remove((r, c))
            
            return res

        # Iterate through every cell on the board to start the search
        for r in range(rows):
            for c in range(cols):
                # We start the DFS only if the first character matches
                if dfs(r, c, 0):
                    return True # Word found!

        # If we finish the loops without finding the word
        return False
        