class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        dist = [n]*n
        prevC = n
        for i in range(n):
            if S[i] == C:
                prevC = i
            if prevC <= i:
                dist[i] = i - prevC
        nextC = -1
        for i in range(n-1,-1,-1):
            if S[i] == C:
                nextC = i
            if nextC >= i:
                dist[i] = min(dist[i], nextC-i)
        return dist