class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        s = {num:idx for idx,num in enumerate(arr)}
        res = 0
        dp = defaultdict(lambda:2) #dp[(i,j)] is the length of longest Fibonacci seq that has last two elements at (i,j)
        for j in range(1,n):
            for i in range(j-1,-1,-1):
                if arr[j]-arr[i]>=arr[i]: break
                if arr[j]-arr[i] in s:
                    k = s[arr[j]-arr[i]]
                    dp[(i,j)] = max(dp[(i,j)], 1+dp[(k,i)])
                res = max(res, dp[(i,j)])             
        return res if res>2 else 0