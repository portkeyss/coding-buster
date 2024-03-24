class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @lru_cache(None)
        def largestPalindromeSeq(start, end):
            if start==end: return 1
            if start>end: return 0
            if s[start]==s[end]:
                return 2+largestPalindromeSeq(start+1, end-1)
            return max(largestPalindromeSeq(start, end-1), 
                       largestPalindromeSeq(start+1, end))
            
        return largestPalindromeSeq(0, len(s)-1)>=len(s)-k