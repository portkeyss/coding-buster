class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = j = 0
        ans = 0
        counter = Counter()
        while j < len(s):
            counter[s[j]] += 1
            majority = max(ct for ct in counter.values())
            while j-i+1-majority > k:
                counter[s[i]] -= 1
                majority = max(ct for ct in counter.values()) 
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans