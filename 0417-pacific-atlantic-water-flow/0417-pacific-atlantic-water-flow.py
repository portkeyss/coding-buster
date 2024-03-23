class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])     
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def flowUpstream(i, j, ocean):
            ocean.add((i,j))
            for d in directions:
                x, y = d[0] + i, d[1] + j
                if x < 0 or x >= m or y < 0 or y >= n or (x,y) in ocean or matrix[x][y] < matrix[i][j]:
                    continue
                flowUpstream(x,y,ocean)
                
        pacific = set()
        atlantic = set()
        for i in range(m):
            flowUpstream(i,0,pacific)
            flowUpstream(i,n-1, atlantic)
        for j in range(n):
            flowUpstream(0,j,pacific)
            flowUpstream(m-1,j, atlantic)
        
        res = []
        for (i,j) in pacific & atlantic:
            res.append([i,j])
        return res       