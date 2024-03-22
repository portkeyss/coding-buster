public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[][] numPath = new int[obstacleGrid.length][obstacleGrid[0].length];
        for (int i = 0; i < obstacleGrid.length && obstacleGrid[i][0] != 1;  i ++) numPath[i][0] = 1;
        for (int j = 0; j < obstacleGrid[0].length && obstacleGrid[0][j] != 1 ; j ++) numPath[0][j] = 1;
        
        for (int i = 1; i < obstacleGrid.length; i ++)
            for (int j = 1; j < obstacleGrid[0].length; j++) {
               if(obstacleGrid[i][j] == 1) numPath[i][j] = 0;
               else numPath[i][j] = numPath[i-1][j] + numPath[i][j-1];
            }
        return numPath[obstacleGrid.length-1][obstacleGrid[0].length-1];
    }
}