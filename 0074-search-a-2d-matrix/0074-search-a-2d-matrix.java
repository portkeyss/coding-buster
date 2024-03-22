public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if ( m ==0 ) return false;
        int n = matrix[0].length;
        int startm = 0, startn = 0; 
        int endm = m - 1, endn = n -1 ;
        while (startm * n + startn <= endm * n + endn) {
            int midm = (((startm + endm ) * n + startn + endn)/2) /n;
            int midn = (((startm + endm ) * n + startn + endn)/2) % n;
            if (matrix[midm][midn] == target) return true;
            else if(matrix[midm][midn] < target) {
                startm = (midm * n + midn + 1) /n;
                startn = (midm * n + midn + 1) % n;
            }
            else {
                 endm = (midm * n + midn - 1) /n;
                 endn = (midm * n + midn - 1) % n;
            }
        }
        return false;
    }
}