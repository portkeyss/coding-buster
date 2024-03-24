class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #BFS
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        q = deque()
        q.append((0,0))
        dist = {}
        dist[(0,0)] = 1
        directions = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        while q:
            i,j = q.popleft()
            if i == n-1 and j == n-1:
                return dist[(i,j)]
            for d in directions:
                x, y = d[0] + i, d[1] + j
                if x < 0 or x >=n or y < 0 or y >= n or (x, y) in dist:
                    continue
                if grid[x][y] == 0:
                    q.append((x,y))
                    dist[(x,y)] = dist[(i,j)] + 1
        return -1
                    