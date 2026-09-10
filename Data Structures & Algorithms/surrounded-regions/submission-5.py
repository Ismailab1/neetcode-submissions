class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or board[row][col] != "O":
                return
            
            board[row][col] = "#"

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                dfs(nr, nc)
        
        for i in range(rows):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][cols - 1] == "O":
                dfs(i, cols - 1)

        for j in range(cols):
            if board[0][j] == "O":
                dfs(0, j)
            if board[rows - 1][j] == "O":
                dfs(rows - 1, j)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"