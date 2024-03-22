class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #preprocessing, trim out excessive "*"'s
        t = []
        cur = ""
        for c in p:
            if c=="*" and cur=="*": continue
            t.append(c)
            cur = c
        p = "".join(t)

        m,n = len(s),len(p)

        @lru_cache(None)
        def match(i,j):#by construction,we never make p[j]=="*"
            if i==m:
                if j==n: return True
                if j+1<n and p[j+1]=="*": return match(i,j+2)
                return False
            if j==n: return False
            if j+1==n or p[j+1]!="*":
                return (s[i]==p[j] or p[j]==".") and match(i+1,j+1)
            if match(i,j+2): return True
            return (s[i]==p[j] or p[j]==".") and (match(i+1,j+2) or match(i+1,j))
        return match(0,0)