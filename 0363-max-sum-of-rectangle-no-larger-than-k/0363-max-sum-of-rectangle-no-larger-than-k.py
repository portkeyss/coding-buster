from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        cumInRow = [[0]*(n+1)]
        for i in range(1,m+1):
            cum = [0]
            for j in range(1,n+1):
                cum.append(cum[-1] + matrix[i-1][j-1])
            cumInRow.append(cum)
        
        res = float('-inf')
        for j in range(n):
            for l in range(j,n):
                sl = SortedList()
                c = 0
                sl.add(0)
                for i in range(m):
                    c += cumInRow[i+1][l+1] - cumInRow[i+1][j]
                    p = sl.bisect_left(c-k) # min upper bound index for c-k
                    if p < len(sl):
                        s = c - sl[p]
                        if s == k:
                            return k
                        res = max(res,s)
                    sl.add(c)
        return res