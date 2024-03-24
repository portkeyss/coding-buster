class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0]*(n+1)
        for j in range(1,n+1):
            dp[j] = dp[j-1]+books[j-1][1]
            w = books[j-1][0]
            h = books[j-1][1]
            for i in range(j-1,0,-1):
                w += books[i-1][0]
                if w>shelfWidth: break
                h = max(h, books[i-1][1])
                dp[j] = min(dp[j], dp[i-1]+h)
        return dp[n]