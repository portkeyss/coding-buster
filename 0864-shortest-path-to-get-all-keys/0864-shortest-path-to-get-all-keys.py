class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        keys = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="@":start = (i,j)
                elif grid[i][j].islower():
                    keys.append(grid[i][j])
        A = {x:i for i,x in enumerate(keys)}
        l = len(keys)
        steps = 0
        state = (start[0],start[1],0)
        q = [state]
        visited = set()
        visited.add(state)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q:
            t = []
            for r,c,s in q:
                for dc,dr in directions:
                    if 0<=r+dr<m and 0<=c+dc<n:
                        state = None
                        if grid[r+dr][c+dc] in ".@":
                            state = (r+dr, c+dc, s)
                        elif grid[r+dr][c+dc].islower():
                            if s|(1<<A[grid[r+dr][c+dc]])==(1<<l)-1: return steps+1
                            state = (r+dr, c+dc, s|(1<<A[grid[r+dr][c+dc]]))
                        elif grid[r+dr][c+dc].isupper():
                            if s&(1<<A[grid[r+dr][c+dc].lower()]):
                                state = (r+dr, c+dc, s)
                        if state and state not in visited:
                            t.append(state)
                            visited.add(state)
            q = t
            steps += 1                         
        return -1