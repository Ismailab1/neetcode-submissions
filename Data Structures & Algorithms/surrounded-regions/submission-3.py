class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(board), len(board[0])

        def dfs(row, col):
            if (row not in range(n) or col not in range(m) or board[row][col] != "O"):
                return
            
            board[row][col] = "#"

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                dfs(nr, nc)
            
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)

        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n - 1][j] == "O":
                dfs(n - 1, j)

        for r in range(n):
            for c in range(m):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"