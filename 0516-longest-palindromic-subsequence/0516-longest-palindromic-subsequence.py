class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        memo = [[None]*m for _ in range(m)]
        def f(i,j):
            if memo[i][j]:
                return memo[i][j]
            if i > j:
                return 0
            if i == j:
                memo[i][j] = 1
            elif s[i] == s[j]:
                memo[i][j] = f(i+1,j-1) + 2
            else:
                memo[i][j] = max(f(i+1,j), f(i,j-1))
            return memo[i][j]
        return f(0, m-1)