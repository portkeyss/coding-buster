class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [1]+[0]*target
        for pr in prob:
            q = [(1-pr)*dp[0]]+[0]*target
            for t in range(1,target+1):
                q[t] = (1-pr)*dp[t]+dp[t-1]*pr
            dp = q
        return dp[target]