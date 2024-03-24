class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        totalOrange = 0
        totalRotten = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten.add((i,j))
                if grid[i][j] != 0:
                    totalOrange += 1
        totalRotten = len(rotten)
        if totalRotten == totalOrange:
            return 0
        
        time = 0
        while totalRotten < totalOrange:
            newRotten = set()
            for (i,j) in rotten:
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    newRotten.add((i-1,j))
                if i+1 < n and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    newRotten.add((i+1,j))
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    newRotten.add((i,j-1))
                if j+1 < m and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    newRotten.add((i,j+1))
            if newRotten:
                totalRotten += len(newRotten)
                rotten = newRotten
                time += 1
            else:
                return -1
        return time