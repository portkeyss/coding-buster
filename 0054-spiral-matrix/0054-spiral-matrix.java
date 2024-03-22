public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list = new ArrayList<Integer>();
        if(matrix.length == 0) return list;
        int m = matrix.length, n = matrix[0].length;
        
        int u = 0, r = n - 1, d = m - 1, l = 0;
        while(list.size() < m * n) {
            if(u == d) {
                for ( int j = l; j <= r; j ++)
                list.add(matrix[u][j]);
            }
            else if (u != d && l == r) {
                  for ( int i = u ; i <= d; i ++)
                  list.add(matrix[i][r]);
            }
            else {
                for ( int j = l; j < r; j ++)
                   list.add(matrix[u][j]);
                for ( int i = u ; i < d; i ++)
                   list.add(matrix[i][r]);
                for ( int j = r ; j > l; j --)
                   list.add(matrix[d][j]);
                for ( int i = d; i > u; i --)
                   list.add(matrix[i][l]);
            }
             u++; r--; d--; l++;
        }
        return list;
    }
}