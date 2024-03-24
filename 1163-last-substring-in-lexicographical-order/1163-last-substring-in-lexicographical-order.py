class Solution:
    def lastSubstring(self, s: str) -> str:
        l = []
        m = ""
        for i in range(len(s)):
            m = max(m, s[i:])
        return m      