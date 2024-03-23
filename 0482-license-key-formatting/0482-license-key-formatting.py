class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        t = S.upper().replace("-", "")
        n = len(t)
        i = n % K
        res = []
        if i > 0:
            res.append(t[:i])
        for j in range(i, n, K):
            res.append(t[j:j+K])
        return "-".join(res)