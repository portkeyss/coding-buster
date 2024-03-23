class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf')]*n for _ in range(m)]
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: 
                    dist[i][j] = 0
                    for d in directions:
                        x, y = d[0]+i, d[1]+j
                        if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1 and dist[x][y] == float('inf'):
                            dist[x][y] = 1
                            q.append((x,y))
        while q:
            node = q.popleft()
            i, j = node[0], node[1]
            for d in directions:
                x, y = d[0]+i, d[1]+j
                if 0 <= x < m and 0 <= y < n and dist[x][y] == float('inf'):
                    dist[x][y] = dist[i][j] + 1
                    q.append((x,y))
        return dist
                            