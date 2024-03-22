class Solution:
    def maxProduct(self, words: List[str]) -> int:
        A = defaultdict(lambda:0) #map a unique letters in a word to the max length
        for word in words:
            mask = 0
            for c in word:
                mask |= (1<<(ord(c)-ord("a")))
            A[mask] = max(A[mask], len(word))
        res = 0
        for m1,l1 in A.items():
            for m2,l2 in A.items():
                if m1&m2==0:
                    res = max(res, l1*l2)
        return res 