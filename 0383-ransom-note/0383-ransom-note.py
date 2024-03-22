class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        A = [0] * 26
        for c in magazine:
            A[ord(c) - ord('a')] += 1
        for c in ransomNote:
            A[ord(c) - ord('a')] -= 1
            if A[ord(c) - ord('a')] < 0:
                return False
        return True