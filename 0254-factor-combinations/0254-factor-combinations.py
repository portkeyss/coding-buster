class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def f(m,start):
            ans = []
            i = start
            while i*i <= m:
                if m%i == 0:
                    ans.append([i,m//i])
                    p = f(m//i,i)
                    if p:
                        for l in p:
                            l.append(i)
                            ans.append(l)
                i += 1
            return ans
        return f(n,2)