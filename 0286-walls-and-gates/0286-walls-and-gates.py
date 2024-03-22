class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #BFS
        INF = (1<<31)-1
        m = len(rooms)
        if m == 0:
            return []
        n = len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            if i-1 >= 0 and rooms[i-1][j] == INF:
                rooms[i-1][j] = rooms[i][j] + 1
                q.append((i-1, j))
            if i+1 < m and rooms[i+1][j] == INF:
                rooms[i+1][j] = rooms[i][j] + 1
                q.append((i+1, j))
            if j-1 >= 0 and rooms[i][j-1] == INF:
                rooms[i][j-1] = rooms[i][j] + 1
                q.append((i, j-1))
            if j+1 < n and rooms[i][j+1] == INF:
                rooms[i][j+1] = rooms[i][j] + 1
                q.append((i, j+1))