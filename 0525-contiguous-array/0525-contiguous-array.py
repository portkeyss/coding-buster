class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        S = [] # will be an n+1 list, the first element will be assigned 0
        last_idx_map = {}
        S.append(0)
        last_idx_map[0] = 0
        for i in range(n):
            s = S[-1] + 1 if nums[i] == 1 else S[-1] - 1
            S.append(s)
            last_idx_map[s] = i+1
        ans = 0
        for j in range(n+1):
            if S[j] in last_idx_map:
                ans = max(ans, last_idx_map[S[j]] - j)
        return ans