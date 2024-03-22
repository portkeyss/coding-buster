public class Solution {
    public void rotate(int[][] matrix) {
        int l = 0; 
        int r = matrix.length - 1;
        while(l < r) {
            for(int i = l; i < r; i++) {
                int temp = matrix[l][i];
                matrix[l][i] = matrix[l+r-i][l];
                matrix[l+r-i][l] = matrix[r][l+r-i];
                matrix[r][l+r-i] = matrix[i][r];
                matrix[i][r] = temp;
            }
            l++; r--;
        }
    }
}