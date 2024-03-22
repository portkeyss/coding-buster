public class Solution {
    public boolean exist(char[][] board, String word) {
        if ( word == "") return false;
        char a = word.charAt(0);
        for ( int i = 0; i < board.length; i ++)
             for (int j = 0; j < board[0].length;  j ++){
                 if (a == board[i][j]){
                     if(word.length() == 1) return true;
                     else {
                         boolean[][] used = new boolean[board.length][board[0].length];
                         used[i][j] = true;
                         if(exist(board, word, 1, i, j, used)) return true;
                         else used[i][j] = false;
                     }
                 }
             }
        return false;
    }
    private boolean exist(char[][] board, String word, int k, int i, int j, boolean[][] used) {
        if (k == word.length()) return true; 
        if (i >= 1 && !used[i-1][j] && board[i-1][j] == word.charAt(k))  {
            used[i-1][j] = true;
            if(exist(board, word, k+1, i-1,j, used)) return true;
            else used[i-1][j] = false;
        }
             
        if (i <= board.length -2 &&!used[i+1][j]  && board[i+1][j] == word.charAt(k)) {
             used[i+1][j] = true;
             if(exist(board, word, k+1, i+1,j, used)) return true;
             else used[i+1][j] = false;
        }
        if (j >= 1 && !used[i][j-1] && board[i][j-1] == word.charAt(k)) {
             used[i][j-1] = true;
             if(exist(board, word, k+1,i,j-1, used)) return true;
             else used[i][j-1] = false;
        }
        if (j <= board[0].length -2 && !used[i][j+1] && board[i][j+1] == word.charAt(k)) {
             used[i][j+1] = true; 
             if(exist(board, word, k+1,i, j+1, used)) return true;
             else used[i][j+1] = false;
        }
        return false;
    }
}