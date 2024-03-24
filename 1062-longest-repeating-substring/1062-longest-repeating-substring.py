class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        def hasRepeat(length):
            st = set()
            for i in range(n-length+1):
                if S[i:i+length] in st: return True
                else: st.add(S[i:i+length])
            return False
        l, r = 0, n-1
        while l<r:
            mid = (l+r+1)//2
            if hasRepeat(mid):
                l = mid
            else:
                r = mid-1
        return l