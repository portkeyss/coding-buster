class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        out_degree = [0] * (N+1)
        in_degree = [0] * (N+1)
        for t in trust:
            out_degree[t[0]] += 1
            in_degree[t[1]] += 1

        for i in range(1,N+1):
            if out_degree[i] == 0 and in_degree[i] == N-1:
                return i
        return -1   