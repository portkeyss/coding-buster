class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [[-1]*(N+1) for _ in range(L+1)]
        def f(i,j):
            if i == j == 0:
                return 1
            if i * j == 0:
                return 0
            if dp[i][j] > -1:
                return dp[i][j]
            ans = f(i-1,j-1)*(N-j+1) + f(i-1, j)*max(0,j-K)
            dp[i][j] = ans
            return ans
        return f(L,N) % (10**9+7)   