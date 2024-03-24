class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisor(s,t):
            if len(s) % len(t) != 0:
                return False
            n = len(s)//len(t)
            a = len(t)
            for i in range(n):
                if t != s[i*a:(i+1)*a]:
                    return False
            return True
        
        for k in range(1, len(str1)+1):
            if len(str1) % k != 0:
                continue
            candidate = str1[:len(str1)//k]
            if isDivisor(str1, candidate) and isDivisor(str2, candidate):
                return candidate
        return ""