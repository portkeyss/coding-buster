class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        def encode(arr):
            mask = 0
            for i in range(m):
                for j in range(n):
                    mask |= (arr[i][j]<<(i*n+j))
            return mask
        
        def neis(mask):
            ans = []
            for i in range(m):
                for j in range(n):     
                    k = i*n+j
                    newMask = mask^(1<<k)
                    if i>0: newMask ^= (1<<((i-1)*n+j))
                    if i<m-1: newMask ^= (1<<((i+1)*n+j))
                    if j>0: newMask ^= (1<<(i*n+j-1))
                    if j<n-1: newMask ^= (1<<(i*n+j+1))
                    ans.append(newMask)
            return ans
        
        start=encode(mat)
        if start==0: return 0
        q = [start]
        seen = set([start])
        step = 0 
        while q:
            t = []
            for x in q:
                for y in neis(x):
                    if y==0: return step+1
                    if y not in seen:
                        t.append(y)
                        seen.add(y)
            q = t
            step += 1
        return -1