public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] aux = new int[m][n];
        aux[0][0] = grid[0][0];
        for(int i = 1; i < m; ++i) aux[i][0] = aux[i-1][0] + grid[i][0];
        for(int j = 1; j < n; ++j) aux[0][j] = aux[0][j-1] + grid[0][j];
        if(m >= n) {
            for(int a = 1; a < n; ++a)
                for(int i = 1; i < a; ++i)
                    aux[i][a-i] = Math.min(aux[i-1][a-i], aux[i][a-i-1]) + grid[i][a-i];
            for(int a = n; a < m; ++a)
                for(int j = 1; j < n; ++j)
                    aux[a-j][j] = Math.min(aux[a-j-1][j], aux[a-j][j-1]) + grid[a-j][j];
            for(int a = m; a < m+n-1; ++a)
                for(int i = a-n+1; i < m; ++i)
                    aux[i][a-i] = Math.min(aux[i-1][a-i], aux[i][a-i-1]) + grid[i][a-i];
        }
        else {
            for(int a = 1; a < m; ++a)
                for(int j = 1; j < a; ++j)
                    aux[a-j][j] = Math.min(aux[a-j][j-1], aux[a-j-1][j]) + grid[a-j][j];
            for(int a = m; a < n; ++a)
                for(int i = 1; i < m; ++i)
                    aux[i][a-i] = Math.min(aux[i][a-i-1], aux[i-1][a-i]) + grid[i][a-i];
            for(int a = n; a < m+n-1; ++a)
                for(int j = a-m+1; j < n; ++j)
                    aux[a-j][j] = Math.min(aux[a-j][j-1], aux[a-j-1][j]) + grid[a-j][j];
        }
        return aux[m-1][n-1];
    }
}