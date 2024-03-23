class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        A = [Counter() for _ in range(n)]
        B = [Counter() for _ in range(n)]
        for j in range(n):
            for i in range(j): 
                d = nums[j]-nums[i]
                A[j][d] += 1
                B[j][d] += (B[i][d]+A[i][d])
                res += (B[i][d]+A[i][d])
        return res