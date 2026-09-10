class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Stores the rows and columns of the sudoku board into
        # a set for O(1) lookup
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        
        # Looks through each row and column and checks if
        # the current position is within the board and
        # if there is a duplicate within the square.
        # If there is a duplicate within the square,
        # we return False
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Adds the current square to the sets to be compared with
                # the others positions
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True
