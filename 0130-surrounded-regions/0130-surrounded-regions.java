public class Solution {
    public void solve(char[][] board) {
        int m = board.length; 
        if(m == 0) return;
        int n = board[0].length;
        
        for(int i = 0; i < m; i++) if(board[i][0] == 'O' ) recordOpenEntries(board,i,0); 
        for(int i = 0; i < m; i++) if(board[i][n-1] == 'O') recordOpenEntries(board,i,n-1); 
        for(int i = 1; i < n-1; i++) if(board[0][i] == 'O') recordOpenEntries(board,0,i); 
        for(int i = 1; i < n-1; i++) if(board[m-1][i] == 'O') recordOpenEntries(board,m-1,i);
        
        for(int i = 0; i < m ; i++) {
            for(int j = 0; j < n ; j++) {
                if(board[i][j] == 'O') board[i][j] = 'X';
                if(board[i][j] == 'S') board[i][j] = 'O';
            }
        }
    }
    private void recordOpenEntries(char[][] board, int i0, int j0) {
                int m = board.length; int n = board[0].length;
                Stack<int[]> q = new Stack<int[]>(); 
                int[] index0 = new int[2]; 
                index0[0] = i0; index0[1] =j0; q.push(index0); 
                while(!q.isEmpty()) { 
                    int[] p = q.pop();
                    board[p[0]][p[1]] = 'S';
                    if(p[0] > 0 && board[p[0] -1][p[1]] == 'O')  
                        {int[] index = new int[2];index[0] =p[0] -1; index[1] =p[1]; q.push(index);} 
                    if(p[0] < m - 1 && board[p[0] +1][p[1]] == 'O')  
                        {int[] index = new int[2];index[0] =p[0] +1; index[1] =p[1]; q.push(index);} 
                    if(p[1] > 0 &&  board[p[0] ][p[1]-1] == 'O')  
                        {int[] index = new int[2];index[0] =p[0]; index[1] =p[1]-1; q.push(index);} 
                    if(p[1] < n - 1 && board[p[0]][p[1]+1] == 'O')  
                        {int[] index = new int[2];index[0] =p[0]; index[1] =p[1]+1; q.push(index);}
                }
    }
}