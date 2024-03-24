class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def longestCommonSubsequence(s1,s2):
            m = len(s1)
            n = len(s2)
            dp = [[""]*(n+1) for _ in range(m+1)]
            for i in range(1,m+1):
                for j in range(1,n+1):
                    if s1[i-1]==s2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+s1[i-1]
                    else:
                        dp[i][j] = dp[i][j-1] if len(dp[i][j-1])>=len(dp[i-1][j]) else dp[i-1][j]
            return dp[m][n]
        
        lcs = longestCommonSubsequence(str1,str2)
        m, n = len(str1), len(str2)
        i = 0
        j = 0
        buf = []
        for k in range(len(lcs)):
            while str1[i]!=lcs[k]:
                buf.append(str1[i])
                i += 1
            while str2[j]!=lcs[k]:
                buf.append(str2[j])
                j += 1 
            buf.append(lcs[k])
            i += 1
            j += 1
        if i<m: buf.append(str1[i:])
        if j<n: buf.append(str2[j:])
        return "".join(buf)  