class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        tot = sum(nums)
        n = len(nums)
        dp = [set() for _ in range(n//2+1)]
        dp[0].add(0)
        for num in nums:
            for k in range(n//2-1,-1,-1):
                if tot*(k+1)%n==0 and tot*(k+1)//n-num in dp[k]: return True
                for sm in dp[k]:
                    dp[k+1].add(sm+num)
        return False