class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        counter = Counter()
        res = 0
        for i,c in enumerate(s):
            counter[c] += 1
            if i>=k:
                counter[s[i-k]] -= 1
                if counter[s[i-k]]==0: counter.pop(s[i-k])
            res += len(counter.keys())==k
        return res