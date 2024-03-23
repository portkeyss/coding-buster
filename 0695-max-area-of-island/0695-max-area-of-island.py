class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        def cal_area(a,b):
            area = 0
            stack = []
            stack.append((a,b))
            grid[a][b] = -1
            while stack:
                p,q = stack.pop()
                area += 1
                if p-1 >= 0 and grid[p-1][q] == 1:
                    stack.append((p-1,q))
                    grid[p-1][q] = -1
                if p+1 < n and grid[p+1][q] == 1:
                    stack.append((p+1,q))
                    grid[p+1][q] = -1
                if q-1 >= 0 and grid[p][q-1] == 1:
                    stack.append((p,q-1))
                    grid[p][q-1] = -1
                if q+1 < m and grid[p][q+1] == 1:
                    stack.append((p,q+1))
                    grid[p][q+1] = -1
                                 
            return area            
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, cal_area(i,j))
        return max_area
                    