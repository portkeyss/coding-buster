class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        j = 0
        dict = {}
        for i in range(len(s)): #each step we find the longest substrings with no repeats that ends at i
            if s[i] in dict:
                j = max(j, dict[s[i]] + 1)

            longest = max(longest, i - j + 1)
            dict[s[i]] = i
        return longest