public class Solution {
    public int uniquePaths(int m, int n) {
        // recursion might exceeds the time constraints, therefore it is better to switch to interation
        /*if (m == 0 || n == 0) return 1;
        if (m > 0 && n > 0) return uniquePaths(m-1, n) + uniquePaths(m, n-1);
        return 0;*/
        if (m == 0 || n == 0) return 1;
        int[][] count = new int[m][n];
        for (int i = 0; i < m; i++) count[i][0] = 1; 
        for (int i = 0; i < n; i++) count[0][i] = 1;   
        for ( int i = 1; i < m; i++)
           for ( int j = 1; j < n; j++)
               count[i][j] = count[i-1][j] + count[i][j-1];
         return count[m-1][n-1];
    }
}