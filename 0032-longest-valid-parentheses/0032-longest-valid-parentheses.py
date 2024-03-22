class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = []
        dp = [0]*(len(s)+1)
        for i,c in enumerate(s):
            if c=="(":
                stack.append(i)
            elif stack:
                j = stack.pop()
                dp[i+1] = i-j+1+dp[j]
                ans = max(ans, dp[i+1])
        return ans