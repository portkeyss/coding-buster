class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ind = {}
        cumSum = [0]
        ind[0] = 0
        for i, n in enumerate(nums):
            a = cumSum[-1] + n
            cumSum.append(a)
            ind[a] = i+1
        ans = 0
        for j, m in enumerate(cumSum):
            if m+k in ind:
                ans = max(ans, ind[m+k] - j)
        return ans    