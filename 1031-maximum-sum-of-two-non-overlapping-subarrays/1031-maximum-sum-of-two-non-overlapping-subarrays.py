class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        leftLMaxSum = self.maxSubarraySum(A, L, M, True)
        leftMMaxSum = self.maxSubarraySum(A, M, L, True)
        rightLMaxSum = self.maxSubarraySum(A, L, M, False)
        rightMMaxSum = self.maxSubarraySum(A, M, L, False)
          
        res = -1
        for i in range(L-1, len(A) - M):
            res = max(res, leftLMaxSum[i]+rightMMaxSum[i+1])
        for i in range(M-1, len(A) - L):
            res = max(res, leftMMaxSum[i]+rightLMaxSum[i+1])
        return res
    
    def maxSubarraySum(self, A, L, M, left):
        if left:
            leftLSum = [0]*len(A)
            leftLSum[L-1] = sum(A[:L])
            leftLMaxSum = [-1] * len(A)
            leftLMaxSum[L-1] = leftLSum[L-1]
            for i in range(L, len(A) - M):
                leftLSum[i] = leftLSum[i-1] - A[i-L] + A[i]
                leftLMaxSum[i] = max(leftLMaxSum[i-1], leftLSum[i])
            return leftLMaxSum
        else:
            return self.maxSubarraySum(A[::-1], L, M, True)[::-1]