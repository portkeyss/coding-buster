class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack = []
        m, n = len(grid), len(grid[0])
        
        def findOne():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return (i,j)
                    
        x,y = findOne()    
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        stack = []
        stack.append((x,y))
        grid[x][y] = 2
        
        p = 0
        while stack:
            a,b = stack.pop()
            for d in directions:
                if a+d[0] < 0 or a+d[0] >= m or b+d[1] < 0 or b+d[1] >= n or grid[a+d[0]][b+d[1]] == 0:
                    p += 1
                elif grid[a+d[0]][b+d[1]] == 1:
                    stack.append((a+d[0], b+d[1]))
                    grid[a+d[0]][b+d[1]] = 2
        
        return p       
        