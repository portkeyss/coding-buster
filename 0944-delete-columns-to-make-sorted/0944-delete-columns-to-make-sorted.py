class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        res = 0
        for i in range(m):
            for j in range(1,n):
                if strs[j][i]<strs[j-1][i]:
                    res += 1
                    break
        return res