public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int i = 0, j = 0;
        int m = matrix.length;
        if(m == 0) return false;
        int n = matrix[0].length;
        while(i < m && j < n ) {
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] > target) return false;
            for(int q = j + 1; q < n; q++) {
                if(matrix[i][q] == target) return true;
                if(matrix[i][q] > target) break;
            }
            for(int p = i + 1; p < m; p++) {
                if(matrix[p][j] == target) return true;
                if(matrix[p][i] > target) break;
            }
            i++; j++;
        }
        return false;
    }
}