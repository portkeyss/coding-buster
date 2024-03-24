class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counter = Counter()
        i = j = 0
        letters = 0
        freq = Counter() 
        while j < len(s):
            counter[s[j]] += 1
            if counter[s[j]] == 1:
                letters += 1
            while letters > maxLetters or j-i + 1 > minSize:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    letters -= 1
                i += 1
            if letters <= maxLetters and maxSize >= j-i+1 >= minSize:
                freq[s[i:j+1]] += 1
            j += 1
        return max(freq.values()) if freq.values() else 0