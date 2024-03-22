class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {   
        int m = board.size(), n = board[0].size();
        vector<vector<int>> result(m, vector<int>(n));
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                int num = 0;
                if(i-1 >= 0){
                    if(board[i-1][j] == 1) num++;
                    if(j-1 >= 0 && board[i-1][j-1] == 1) num++;
                    if(j+1 < n && board[i-1][j+1] == 1) num++;
                }
                if(j-1 >= 0 && board[i][j-1] == 1) num++;
                if(j+1 < n && board[i][j+1] == 1) num++;
                if(i+1 < m){
                    if(board[i+1][j] == 1) num++;
                    if(j-1 >= 0 && board[i+1][j-1] == 1) num++;
                    if(j+1 < n && board[i+1][j+1] == 1) num++;
                }
                if(board[i][j] == 1){
                    if(num < 2) result[i][j] = 0;
                    else if(num <= 3) result[i][j] = 1;
                    else result[i][j] = 0;
                }else{
                    if(num == 3) result[i][j] = 1;
                }
            }
        board = result;
        return;
    }
};