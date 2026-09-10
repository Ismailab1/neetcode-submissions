class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_lp, row_rp = 0, len(matrix)
        ROW = -1

        while row_lp < row_rp:
            mid = row_lp + (row_rp - row_lp) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                ROW = mid
                break

            elif matrix[mid][0] > target:
                row_rp = mid

            else:
                row_lp = mid + 1

        if ROW == -1:
            return False
        
        col_lp, col_rp = 0, len(matrix[0])

        while col_lp < col_rp:
            COL = col_lp + (col_rp - col_lp) // 2

            if matrix[ROW][COL] == target:
                return True
            
            elif matrix[ROW][COL] < target:
                col_lp = COL + 1
            
            else:
                col_rp = COL

        return False