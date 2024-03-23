class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        #BFS
        m, n = len(A), len(A[0])
        def findFirstIsland():
            for i in range(m):
                for j in range(n):
                    if A[i][j] == 1:
                        return (i,j)
        
        i,j = findFirstIsland()
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        stack = []
        stack.append((i,j))
        A[i][j] = 2
        q = collections.deque()
        dist = dict()
        while stack:#traverse all cell in this island, mark every cell value 2, and store boundary cells in a queue
            x,y = stack.pop()
            for d in directions:
                if 0 <= x + d[0] < m and 0 <= y + d[1] < n:
                    if A[x+d[0]][y + d[1]] == 0:
                        q.append((x+d[0], y+d[1]))
                        dist[(x+d[0],y + d[1])] = 0
                    elif A[x+d[0]][y + d[1]] == 1:
                        stack.append((x+d[0], y+d[1]))
                        A[x+d[0]][y + d[1]] = 2
        
        while q:
            x,y = q.popleft()
            for d in directions:
                if 0 <= x + d[0] < m and 0 <= y + d[1] < n:
                    if (x+d[0], y+d[1]) not in dist:                     
                        dist[(x+d[0], y+d[1])] = 1 + dist[(x,y)]
                        if A[x+d[0]][y+d[1]] == 1:
                            return dist[(x+d[0],y+d[1])]
                        q.append((x+d[0], y+d[1]))
            
       
            