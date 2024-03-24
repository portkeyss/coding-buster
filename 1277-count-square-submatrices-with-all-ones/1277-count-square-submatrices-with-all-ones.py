class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        consec_ones_in_row = [[0]*(n+1) for _ in range(m+1)]
        consec_ones_in_col = [[0]*(n+1) for _ in range(m+1)]
        largest_square_len = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    consec_ones_in_row[i+1][j+1] = consec_ones_in_row[i][j+1] + 1
                    consec_ones_in_col[i+1][j+1] = consec_ones_in_col[i+1][j] + 1
                    largest_square_len[i+1][j+1] = min(consec_ones_in_row[i+1][j+1], consec_ones_in_col[i+1][j+1], 1+largest_square_len[i][j])
                    ans += largest_square_len[i+1][j+1]
        return ans    