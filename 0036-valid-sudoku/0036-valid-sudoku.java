public class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character> hs = new HashSet<Character>();
        for(int i = 0; i < board.length; i ++) {
            hs.clear();
           for(int j = 0; j< board[0].length; j ++) {
               if(board[i][j] != '.') {
                   if(hs.contains(board[i][j])) return false;
                   else hs.add(board[i][j]);
               }
           }
        }
         for(int j = 0; j< board[0].length; j ++) {
              hs.clear();
              for(int i = 0; i < board.length; i ++) {
                  if(board[i][j] != '.') {
                      if(hs.contains(board[i][j])) return false;
                      else hs.add(board[i][j]);
                   }
               }
         }
         for(int i = 0; i < 9; i = i + 3) 
              for(int j = 0; j < 9; j = j + 3) {
            hs.clear();
           for(int k = i; k < i + 3; k ++) 
               for(int l = j; l < j + 3; l ++) {
               if(board[k][l] != '.') {
                   if(hs.contains(board[k][l])) return false;
                   else hs.add(board[k][l]);
               }
           }
        }
        return true;
    }
}