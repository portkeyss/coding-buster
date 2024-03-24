class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n, m = len(workers), len(bikes)
        md = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                md[i][j] = abs(workers[i][0]-bikes[j][0])+abs(workers[i][1]-bikes[j][1])
                
        def getOnes(x):
            count = 0
            while x:
                x &= x-1
                count += 1
            return  count
        
        dp = [inf]*(1<<m)
        dp[0]=0
        res = inf
        for mask in range(1,1<<m):
            p = getOnes(mask)
            if p>n: continue
            for j in range(m):
                if (1<<j)&mask:
                    dp[mask]= min(dp[mask],dp[mask^(1<<j)]+md[p-1][j])
                    if p==n: res = min(res, dp[mask])
        return res