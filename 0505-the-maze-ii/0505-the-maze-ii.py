class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m,n  = len(maze), len(maze[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        q = deque()
        distance = defaultdict(lambda:float('inf'))
        q.append(tuple(start))
        distance[tuple(start)] = 0
        
        while q:
            s0, s1 = q.popleft()
            for d in directions:
                x, y = s0, s1
                while 0 <= x+d[0] < m and 0 <= y+d[1] < n and maze[x+d[0]][y+d[1]] == 0:
                    x += d[0]
                    y += d[1]     
                if x == s0 and y == s1: #does not move in the given direction
                    continue
                if distance[(s0,s1)] + abs(x-s0) + abs(y-s1) < distance[(x,y)]:
                    distance[(x,y)] = distance[(s0,s1)] + abs(x-s0) + abs(y-s1)
                    q.append((x,y))
        return distance[tuple(destination)] if distance[tuple(destination)] < float('inf') else -1