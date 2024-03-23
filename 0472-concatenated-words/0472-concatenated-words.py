class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)
        def check(w):
            n = len(w)
            if n == 0:
                return False
            dp = [False]*(n+1)
            dp[0] = True
            for i in range(n):
                for j in range(i,-1,-1):
                    if dp[j] and w[j:i+1] in dictionary:
                        dp[i+1] = True
                        break
            return dp[n]
        
        res = []
        for word in words:
            dictionary.remove(word)
            if check(word):
                res.append(word)
            dictionary.add(word)
        return res