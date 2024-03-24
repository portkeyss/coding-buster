class Solution:
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        mod = 10**9+7
        def rabinKarp(length):
            h = 0
            bit = 1
            for i in range(length):
                h = (26*h%mod +(ord(S[i])-ord('a')))%mod
                bit = (26*bit) % mod
            A = {h:0}
            for i in range(length,n):
                h = (26*h%mod +(ord(S[i])-ord('a'))-((ord(S[i-length])-ord('a'))*bit)%mod)%mod
                if h in A and S[A[h]:A[h]+length]==S[i-length+1:i+1]: return S[A[h]:A[h]+length]
                A[h]=i-length+1
            return ""
        
        l, r = 0,n-1
        res = ""
        while l<r:
            m = (l+r+1)//2
            t = rabinKarp(m)
            if len(t)>len(res):
                res = t
                l = m
            else:
                r = m-1
        return res