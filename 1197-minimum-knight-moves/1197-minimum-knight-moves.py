class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        #BFS for shortest path
        
        IFNTY = 10**10
        dp = defaultdict(lambda:IFNTY) #dynamical programming that stores shortest path already calculated
        dp[(0,0)] = 0
        
        # path and write path are introduced to take advantage of symmetry. We do not need to store any (a,b) pair calculated in dynamical programming. We can in fact refer to the equivalent ones. These two functions ensures that we are operating on a black box, encapsulating all symmetry features inside these functions,while keeping other parts of the code clean and concise.
        def path(a: int, b:int) -> int:            
            # due to symmetry, we can make such simplications
            a,b = abs(a), abs(b) 
            if a < b:
                a, b = b, a
            return dp[(a,b)]
        
        def write_path(a: int, b:int, dist: int) -> int:            
            # due to symmetry, we can make such simplications
            a,b = abs(a), abs(b) 
            if a < b:
                a, b = b, a
            dp[(a,b)] = dist
        
        directions = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
        q = collections.deque()        
        q.append((0,0))
        
        while q:
            n_x, n_y = q.popleft()
            
            for direction in directions:
                nei_x, nei_y = n_x+direction[0],n_y+direction[1]
                if path(nei_x, nei_y) == IFNTY:
                    q.append((nei_x,nei_y))
                    write_path(nei_x, nei_y, 1 + path(n_x, n_y))
            
            if path(x,y) < IFNTY:
                return path(x,y)
            
        return -1