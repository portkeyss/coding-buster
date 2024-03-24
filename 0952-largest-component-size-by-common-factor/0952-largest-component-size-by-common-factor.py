class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        parent = [-1]*n
        rank = [0]*n
        def findPar(x):
            if parent[x]==-1: return x
            parent[x] = findPar(parent[x])
            return parent[x]
        
        def findFactors(x):
            if x==1: return []
            factors = [x]
            for y in range(2,int(sqrt(x))+1):
                if x%y==0: 
                    factors.append(y)
                    if y*y != x:
                        factors.append(x//y)
            return factors
        
        A = dict()
        for i,num in enumerate(nums):
            l = findFactors(num)
            for p in l:
                if p not in A:
                    A[p] = i
                else:
                    x = findPar(A[p])
                    y = findPar(i)
                    if x==y: continue
                    if rank[x]<rank[y]:
                        parent[x]=y
                    elif rank[x]>rank[y]:
                        parent[y]=x
                    else:
                        parent[y] = x
                        rank[x] += 1
        counter = Counter()
        for i in range(n):
            counter[findPar(i)] += 1
        return max(counter.values())  