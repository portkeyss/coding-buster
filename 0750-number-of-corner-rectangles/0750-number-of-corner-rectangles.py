class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        counter = Counter()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0: continue
                for k in range(j+1,n):
                    if grid[i][k]==0: continue
                    res += counter[j,k]
                    counter[j,k] += 1
        return res