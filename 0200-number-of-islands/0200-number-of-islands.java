public class Solution {
    public int numIslands(char[][] grid) {
        int num = 0;
        HashSet<Integer> mark = new HashSet<Integer>();
        int m = grid.length;
        if(m == 0) return 0;
        int n = grid[0].length;
        for(int i = 0; i < m; i++) 
            for(int j = 0; j < n; j++) {
                if(grid[i][j] == '1') mark.add(i * n + j);
            }
        if(mark.isEmpty()) return 0;
        while(!mark.isEmpty()) {
            num++;
            int k = mark.iterator().next();
            union(n,mark,k);
        }
        return num;
    }
    private void union(int n, HashSet<Integer> mark, int k ) {
        int i = k / n, j = k % n;
        mark.remove(k);
        if(mark.contains((i-1) * n + j)) union(n, mark,(i-1) * n + j);
        if(mark.contains((i+1) * n + j)) union(n, mark,(i+1) * n + j);
        if(j >= 1 && mark.contains(i * n + j - 1)) union(n, mark,i * n + j - 1);//note that the bound j>=1 must be included,or it may point to the last entry of the previous row,not the the previous element of the same row, as one really meant to deal with
        if(j <= n - 2 && mark.contains(i * n + j + 1)) union(n, mark,i * n + j + 1);//bound must be included, reason similar to above
    }
}