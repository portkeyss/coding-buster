class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[1,0],[0,-1],[-1,0],[0,1]]
        
        def dfs(x,y, walls, exposures,island):
            island.add((x,y))
            for d in directions:
                a, b = x+d[0], y+d[1]
                if 0 <= a < m and 0 <= b < n and (a, b) not in island:
                    if grid[a][b] == 1:
                        dfs(a, b, walls, exposures, island)
                    elif grid[a][b] == 0:
                        walls[0] += 1
                        exposures.add((a, b))       
        
        totWalls = 0
        while True:
            visited = set()
            nextInfect = defaultdict()
            c = [-1,-1, 0, set()] # candidate of area that can infect largest cells: [x, y, wall, island]
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        continue
                    if grid[i][j] == 1 and (i,j) not in visited:
                        walls = [0]
                        exposures =  set()
                        island = set()
                        dfs(i, j, walls, exposures, island)
                        if c[0] == -1 or len(nextInfect[(c[0], c[1])]) < len(exposures):
                            c = [i,j, walls[0], island]
                        visited.update(island)
                        nextInfect[(i,j)] = exposures
        
            if c[0] == -1: 
                return totWalls
            totWalls += c[2]
            
            for i,j in c[3]:#permanently isolated
                grid[i][j] = 2 
     
            for (i,j), exposures in nextInfect.items():
                if i == c[0] and j == c[1]:
                    continue
                for (x,y) in exposures:
                    grid[x][y] = 1     
            
            