class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return 0
        if k>=m+n-3: return m+n-2
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        q.append((0,0,k,0))
        visited = set()
        visited.add((0,0,k))
        while q:
            i, j, credit, step = q.popleft()
            for d in directions:
                r,c = i+d[0], j+d[1]
                if r<0 or r>=m or c<0 or c>=n:
                    continue
                newCredit = credit-grid[r][c]
                if newCredit >= 0 and (r, c, newCredit) not in visited:
                    if r==m-1 and c==n-1:
                        return 1+step
                    q.append((r,c,newCredit, 1+step)) 
                    visited.add((r,c, newCredit))
        return -1