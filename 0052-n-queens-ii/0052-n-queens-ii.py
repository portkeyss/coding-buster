class Solution:
    def totalNQueens(self, n: int) -> int:
        def f(cur,available,diag,antiDiag):
            if len(cur)==n: 
                return 1
            i = len(cur)
            ans = 0
            for j in available:
                if i+j not in diag and i-j not in antiDiag:
                    ans += f(cur+[j], available-{j},diag|{i+j},antiDiag|{i-j})
            return ans

        return f([],{i for i in range(n)},set(),set())    