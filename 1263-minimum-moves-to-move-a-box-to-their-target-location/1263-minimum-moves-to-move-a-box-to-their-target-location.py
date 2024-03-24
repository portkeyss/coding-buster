class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        s,b,t = None, None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="S": s = (i,j)
                elif grid[i][j]=="B": b = (i,j)
                elif grid[i][j]=="T": t = (i,j)
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def f(bx,x):#return the neighboring positions of box that can be reached by player
            q1 = deque()
            q1.append(x)
            seen = set()
            seen.add(x)
            l = []
            while q1:
                y = q1.popleft()
                if abs(y[0]-bx[0])+abs(y[1]-bx[1])==1:
                    l.append(y)
                for dr,dc in directions:
                    z,w = y[0]+dr, y[1]+dc
                    if 0<=z<m and 0<=w<n and (z,w) not in seen and grid[z][w]!="#" and (z,w)!=bx:
                        q1.append((z,w))
                        seen.add((z,w))
            return l
        
        visited = set()
        q = []
        steps = 0
        for player in f(b,s):
            q.append((b,player))
            visited.add((b,player))
        while q:
            temp = []
            for box,player in q:
                newBox, newPlayer = (2*box[0]-player[0], 2*box[1]-player[1]), box
                if 0<=newBox[0]<m and 0<=newBox[1]<n:
                    if grid[newBox[0]][newBox[1]]=="T": return 1+steps
                    if grid[newBox[0]][newBox[1]]!="#":
                        for a in f(newBox, newPlayer):
                            if (newBox,a) not in visited:
                                temp.append((newBox,a))
                                visited.add((newBox,a))
            q = temp
            steps += 1
        return -1