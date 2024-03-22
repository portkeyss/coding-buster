class Solution {
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if(m == 0) return 0;
        int n = matrix[0].size();
        if(n == 0) return 0;
        vector<vector<int>> l(m, vector<int>(n, 0));
        int longest = 1;
         for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                longest = max(longest, lip(matrix, l, i,j,m,n));
            }
         }
        return longest;
        
    }
private:
    int lip(vector<vector<int>>& matrix, vector<vector<int>>& l, int i, int j, int m, int n){          
        if(l[i][j] > 0) return l[i][j];
        l[i][j] = 1;
        if(j+1 < n && matrix[i][j] < matrix[i][j+1]) {
            l[i][j] = max(l[i][j], 1 + lip(matrix, l, i,j+1,m,n));
        }
        if(j-1 > -1 && matrix[i][j] < matrix[i][j-1]) {
            l[i][j] = max(l[i][j], 1 + lip(matrix, l, i,j-1,m,n));
        }
        if(i+1 < m && matrix[i][j] < matrix[i+1][j]) {
            l[i][j] = max(l[i][j], 1 + lip(matrix, l, i+1,j,m,n));
        }
        if(i-1 > -1 && matrix[i][j] < matrix[i-1][j]) {
            l[i][j] = max(l[i][j], 1 + lip(matrix, l, i-1,j,m,n));
        }
        return l[i][j];
    }
};