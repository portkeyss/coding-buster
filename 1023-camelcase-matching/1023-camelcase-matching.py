class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(q,p):
            m,n = len(q),len(p)
            i = j = 0
            while i<m and j<n:
                if q[i]==p[j]:
                    i+=1
                    j+=1
                elif q[i].isupper():
                    return False
                else:
                    i+=1
            if i==m: return j==n
            while i<m and q[i].islower():
                i += 1
            return i==m
        
        return map(lambda x:check(x,pattern), queries)