class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        m = len(M)
        if m == 0:
            return 0
        n = len(M[0])
        
        horizontal = defaultdict(lambda:0)
        vertical = defaultdict(lambda:0)
        diagonal = defaultdict(lambda:0)
        antiDiagonal = defaultdict(lambda:0)
        
        ans = 0     
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0:
                    horizontal[i] = 0
                    vertical[j] = 0
                    diagonal[i-j] = 0
                    antiDiagonal[i+j] = 0
                else:
                    horizontal[i] += 1
                    vertical[j] += 1
                    diagonal[i-j] += 1
                    antiDiagonal[i+j] += 1
                    ans = max(ans, horizontal[i], vertical[j], diagonal[i-j], antiDiagonal[i+j])
        return ans