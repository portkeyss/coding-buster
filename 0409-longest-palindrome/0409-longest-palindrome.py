class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        hasOddCount = False
        length = 0
        for ct, ct in counter.items():
            length += ct
            if ct % 2 == 1:
                length -= 1
                hasOddCount = True
        return length+1 if hasOddCount else length