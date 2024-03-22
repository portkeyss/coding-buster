class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        def f(cur,available,diag,antiDiag):
            if len(cur)==n: 
                A = [["."]*n for _ in range(n)]
                for i,j in enumerate(cur):
                    A[i][j] = "Q"
                A = ["".join(a) for a in A]
                self.res.append(A)
                return
            i = len(cur)
            for j in available:
                if i+j not in diag and i-j not in antiDiag:
                    f(cur+[j], available-{j},diag|{i+j},antiDiag|{i-j})

        f([],{i for i in range(n)},set(),set())
        return self.res     