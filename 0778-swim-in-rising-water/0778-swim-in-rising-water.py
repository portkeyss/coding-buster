class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n==1: return 0
        ds = [[1,0],[0,1],[-1,0],[0,-1]]
        T = set(grid[i][j] for i in range(n) for j in range(n))
        T = sorted(list(T))
        for t in T:
            if grid[0][0]>t: continue
            visited = set((0,0))
            q = deque([(0,0)])
            while q:
                r,c = q.popleft()
                for dx,dy in ds:
                    if 0<=r+dx<n and 0<=c+dy<n and (r+dx,c+dy) not in visited and grid[r+dx][c+dy]<=t:
                        if r+dx==n-1 and c+dy==n-1: return t
                        q.append(((r+dx,c+dy)))
                        visited.add((r+dx,c+dy))