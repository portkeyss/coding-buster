class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)//2
        A = {p:i for i,p in enumerate(row)}
        ans = 0
        for i in range(0,2*n,2):
            if abs(row[i]-row[i+1])==1 and row[i]//2==row[i+1]//2: continue
            else:
                v = row[i]+1 if row[i]%2==0 else row[i]-1
                j = A[v]
                row[i+1], row[j] = row[j], row[i+1]
                A[row[i+1]], A[row[j]] = i+1, j
                ans += 1
        return ans