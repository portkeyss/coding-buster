class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        mp = dict()
        for i in range(len(arr)):
            mp[(i,i)] = arr[i]
            for j in range(i+1, len(arr)):
                mp[(i,j)] = max(mp[(i,j-1)], arr[j])  
        
        dp = dict()
        def f(start, end):
            if start == end:
                return 0
            if (start, end) in dp:
                return dp[start, end]
            mi = 2**31
            for i in range(start, end):
                a = f(start, i) + f(i+1, end) + mp[(start,i)] * mp[(i+1, end)]
                mi = min(mi, a)
            dp[(start,end)] = mi
            return mi
        return f(0, len(arr) - 1)