class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount = 0
        A = dict()
        A[0]=1
        for n in nums:
            if n%2 == 0:
                A[oddCount]+=1
            else:
                oddCount += 1
                A[oddCount] = 1
        res = 0
        for i in range(oddCount):
            if i+k in A:
                res += A[i]*A[i+k]
        return res