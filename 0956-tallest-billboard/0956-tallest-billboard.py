class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for r in rods:
            tmp = Counter()
            for d,h in dp.items():
                tmp[d] = max(tmp[d],h)
                tmp[d+r] = max(tmp[d+r],h+r)
                tmp[abs(d-r)] = max(tmp[abs(d-r)],max(h,h-d+r))
            dp = tmp
        return dp[0]