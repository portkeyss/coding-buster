class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m,n = len(maze), len(maze[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def explore(i,j,e0, e1, seen):
            if i == e0 and j == e1:
                return True
            if (i,j) in seen:
                return False
            seen.add((i,j))
            for d in directions:
                x, y = i,j
                while x+d[0] >= 0 and x+d[0] < m and y+d[1] >= 0 and y+d[1] < n and maze[x+d[0]][y+d[1]] == 0:
                    x += d[0]
                    y += d[1]
                if explore(x,y,e0,e1,seen):
                    return True
            return False
        seen = set()
        return explore(start[0],start[1], destination[0], destination[1], seen)