class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        rows, cols = len(board), len(board[0])
        
        # A set to keep track of visited cells in the current path
        # This prevents using the same letter twice in one path
        path = set()

        def dfs(pos_x, pos_y, i):
            if i == len(word):
                return True
            
            if (pos_x < 0 or pos_y < 0 or pos_x >= rows or pos_y >= cols or word[i] != board[pos_x][pos_y] or (pos_x, pos_y) in path):
                return False
            
            path.add((pos_x, pos_y))

            res = (dfs(pos_x + 1, pos_y, i + 1) or
                   dfs(pos_x - 1, pos_y, i + 1) or
                   dfs(pos_x, pos_y + 1, i + 1) or
                   dfs(pos_x, pos_y - 1, i + 1))

            path.remove((pos_x, pos_y))

            return res


        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
        