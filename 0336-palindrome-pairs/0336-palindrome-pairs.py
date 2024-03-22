class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rev = dict()
        for i, w in enumerate(words):
            rev[w[::-1]] = i
        def isPalindrome(word, s, e):
            p, q = s, e
            while p < q:
                if word[p] != word[q]:
                    return False
                p += 1
                q -= 1
            return True
        
        res = set()
        for i, w in enumerate(words):
            for k in range(len(w)+1):
                if w[:k] in rev and isPalindrome(w, k, len(w)-1):
                    j = rev[w[:k]]
                    if j != i:
                        res.add((i, j))
                if w[k:] in rev and isPalindrome(w, 0, k-1):
                    j = rev[w[k:]]
                    if j != i:
                        res.add((j,i))
        
        res = [[i,j] for (i,j) in res]        
        return res