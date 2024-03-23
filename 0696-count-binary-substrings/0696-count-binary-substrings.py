class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i = 0
        prevLen = 0
        ans = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] == s[i]:
                j += 1
            ans += min(prevLen, j-i)
            prevLen = j-i
            prevLen = j-i
            i = j
        return ans