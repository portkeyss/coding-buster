class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        prob = [[0]*N for _ in range(N)]
        prob[r][c] = 1
        print(prob)
        directions = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        for step in range(1, K+1):
            cur_prob = [[0]*N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for d in directions:
                        x, y = d[0]+i, d[1]+j
                        if 0<=x<N and 0<=y<N:
                            cur_prob[i][j] += prob[x][y]/8
            prob = cur_prob
            print(prob)
        return sum(prob[m][n] for m in range(N) for n in range(N))