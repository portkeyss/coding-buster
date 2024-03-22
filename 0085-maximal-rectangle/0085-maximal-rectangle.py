class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [0]*n
        res = 0
        for i in range(m):
            stack = [-1]
            for j in range(n):
                dp[j] = (1+dp[j])*(matrix[i][j]=="1")
                while stack[-1]!=-1 and dp[stack[-1]]>dp[j]:
                    h = dp[stack.pop()]
                    w = j-1-stack[-1]
                    res = max(res,h*w)
                stack.append(j)
            while stack[-1]!=-1:
                h = dp[stack.pop()]
                w = n-1-stack[-1]
                res = max(res,h*w)
        return res