class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        lp, rp = 0, (ROWS * COLS) - 1

        while lp <= rp:
            mid = lp + (rp - lp) // 2

            col = mid % COLS
            row = mid // COLS
            val = matrix[row][col]

            if val == target:
                return True

            elif val > target:
                rp = mid - 1
            
            else:
                lp = mid + 1

        return False