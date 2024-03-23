class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for l in range(1, n // 2 + 1):
            if not n % l:
                i = 1
                while (i+1)*l <= n and s[:l] == s[i*l : (i+1)*l]:
                    i += 1
                if (i+1)*l > n:
                    return True
        return False
            