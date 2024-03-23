class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        P = [0]*n
        A = [[0,0] for _ in range(n)]
        B = [[0,0] for _ in range(n)]
        C = [[0,0] for _ in range(n)]
        P[n-k] = sum(nums[-k:])
        A[n-k] = [n-k,P[n-k]]
        for i in range(n-k-1,-1,-1):
            P[i] = P[i+1]+nums[i]-nums[i+k]
            if P[i]>=A[i+1][1]:
                A[i] = [i,P[i]]
            else:
                A[i] = [A[i+1][0],A[i+1][1]]
            if i<=n-2*k:
                if P[i]+A[i+k][1]>=B[i+1][1]:
                    B[i] = [i, P[i]+A[i+k][1]]
                else:
                    B[i] = [B[i+1][0],B[i+1][1]]
            if i<=n-3*k:
                if P[i]+B[i+k][1]>=C[i+1][1]:
                    C[i] = [i, P[i]+B[i+k][1]]
                else:
                    C[i] = [C[i+1][0],C[i+1][1]]
        res = [0]*3
        res[0] = C[0][0]
        res[1] = B[res[0]+k][0]
        res[2] = A[res[1]+k][0]
        return res