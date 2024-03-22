public class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        if(m == 0) return 0;
        int n = matrix[0].length;
        int[][] aux1 = new int[m+1][n+1];//record consecutive '1's ending at (i,j) in a row
        int[][] aux2 = new int[m+1][n+1];//record consecutive '1's ending at (i,j) in a col
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                if(matrix[i-1][j-1] == '0') aux1[i][j] = 0;
                else aux1[i][j] = aux1[i][j - 1] + 1;
            }
        }
        for(int j = 1; j <= n; j++) {
            for(int i = 1; i <= m; i++) {
                if(matrix[i-1][j-1] == '0') aux2[i][j] = 0;
                else aux2[i][j] = aux2[i-1][j] + 1;
            }
        }
        int maxEdge = 0;
        int[][] aux3 = new int[m+1][n+1];//record the edge of the largest square ending at (i,j)
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                if(matrix[i-1][j-1] == 0) continue;
                aux3[i][j] = Math.min(aux3[i-1][j-1] + 1,Math.min(aux1[i][j], aux2[i][j]));
                maxEdge = Math.max(maxEdge,aux3[i][j]);
            }
        }
        return maxEdge * maxEdge;
    }
}