public class Solution {
    public void setZeroes(int[][] matrix) {
        boolean row0 = false, col0 = false;
        for(int i = 0; i < matrix.length; i++)  
            if (matrix[i][0] == 0) {
                col0 = true;
                break;
          }
        for(int j = 0; j < matrix[0].length; j++)  
             if (matrix[0][j] == 0) {
                row0 = true;
                break;
          }
          
          
        for(int i = 1; i < matrix.length; i++)
            for(int j = 1; j < matrix[0].length; j++) 
                if (matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
                
                
        for (int i = 1; i < matrix.length; i++) 
            if(matrix[i][0] == 0) {
                for(int j = 1; j < matrix[0].length; j++)
                     matrix[i][j] = 0;
            }
         for (int j = 1; j < matrix[0].length; j++) 
            if(matrix[0][j] == 0) {
                for(int i = 1; i < matrix.length; i++)
                     matrix[i][j] = 0;
            }
        
      if(col0) for(int i = 0; i < matrix.length; i++) matrix[i][0] = 0;
      if(row0) for(int j = 0; j < matrix[0].length; j++) matrix[0][j] = 0;
    }
}