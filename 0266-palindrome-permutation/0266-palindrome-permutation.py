class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        oddCount = 0
        for n in counter.values():
            if n % 2 == 1:
                oddCount += 1
                if oddCount > 1:
                    return False
        return True