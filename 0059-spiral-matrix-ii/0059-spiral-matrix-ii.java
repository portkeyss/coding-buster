public class Solution {
    public int[][] generateMatrix(int n) {
        int u = 0, r = n - 1, d = n - 1, l = 0;
        int[][] matrix = new int[n][n];
        int entry = 1;
        while(entry <= n * n) {
            if(u == d) matrix[u][u] = entry++;
            else {
                for ( int j = l; j < r; j ++)
                   matrix[u][j] = entry++;
                for ( int i = u ; i < d; i ++)
                   matrix[i][r] = entry++;
                for ( int j = r ; j > l; j --)
                   matrix[d][j] = entry++;
                for ( int i = d; i > u; i --)
                   matrix[i][l] = entry ++;
            }
             u++; r--; d--; l++;
        }
        return matrix;
    }
}