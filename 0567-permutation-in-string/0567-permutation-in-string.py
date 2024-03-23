class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        freq1 = [0] * 26
        for c in s1:
            freq1[ord(c) - ord('a')] += 1
        freq2 = [0] * 26
        for i in range(m):
            freq2[ord(s2[i]) - ord('a')] += 1
            
        for j in range(n-m+1):         
            permutation = True
            for i in range(26):
                if freq1[i] != freq2[i]:
                    permutation = False
                    break
            if permutation:
                return True
            if j < n - m:
                freq2[ord(s2[j]) - ord('a')] -= 1
                freq2[ord(s2[j+m]) - ord('a')] += 1
        return False            