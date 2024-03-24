class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [[0]*26 for _ in range(len(s)+1)]
        for i, c in enumerate(s):
            for m in range(26):
                prefix[i+1][m] = prefix[i][m]
            prefix[i+1][ord(c)-ord('a')] += 1
        def chk(l, r, k):
            oddchars = sum((prefix[r+1][p]-prefix[l][p])%2 for p in range(26))
            return oddchars <= 2 * k + 1
        return [chk(q[0], q[1], q[2]) for q in queries]