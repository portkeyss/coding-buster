class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        dic1 = dict()
        dic2 = dict()
        m, n = len(pattern), len(s)
        def f(i,j):
            if i==m: return j==n
            if pattern[i] in dic1:
                if s[j:].startswith(dic1[pattern[i]]):
                    l = len(dic1[pattern[i]])
                    if f(i+1,j+l):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                for k in range(j,n):
                    if s[j:k+1] not in dic2:
                        dic1[pattern[i]] = s[j:k+1]
                        dic2[s[j:k+1]] = pattern[i]
                        if f(i+1, k+1):
                            return True
                        else:
                            dic1.pop(pattern[i])
                            dic2.pop(s[j:k+1])
            return False
        return f(0,0)