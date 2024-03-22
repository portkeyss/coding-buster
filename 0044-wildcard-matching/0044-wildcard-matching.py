class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        t = []
        for i,c in enumerate(p):
            if c=="*" and i>0 and p[i-1]=="*": continue
            t.append(c)
        p = "".join(t)
        m,n = len(s), len(p)

        @lru_cache(None)
        def f(i,j):
            if i==m: return j==n or p[j:]=="*"
            if j==n: return i==m
            if p[j]=="?": return f(i+1,j+1)
            if p[j]=="*": return f(i,j+1) or f(i+1,j)
            return s[i]==p[j] and f(i+1,j+1)
        
        return f(0,0)