class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        if s1==s2: return 0
        n = len(s1)
        d = 0
        q = [s1]
        visited = set([s1])
        while q:
            t = []
            for x in q:
                i = 0
                while i<n and x[i]==s2[i]: i+=1
                for j in range(i+1,n):
                    if x[j]!=s2[j] and x[j]==s2[i]:
                        y = x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
                        if y==s2: return d+1
                        if y not in visited:
                            t.append(y)
                            visited.add(y)
            q = t
            d += 1