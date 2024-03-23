class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int: 
        N = len(board)
        asc = 1
        flattened = [-1]
        for i in range(N-1, -1, -1):
            rge = range(N) if asc == 1 else range(N-1,-1,-1)
            for j in rge:
                flattened.append(board[i][j])
            asc *= -1
        #print(flattened)    
        q = collections.deque()
        q.append(1)
        move = dict()
        move[1] = 0
        while q:
            m = q.popleft()
            for i in range(1,7):
                if m+i > N*N:
                    continue
                if flattened[m+i] == -1 and m + i in move:
                    continue
                if flattened[m+i] != -1 and flattened[m+i] in move:
                    continue
                n = m + i if flattened[m+i] == -1 else flattened[m+i]
                move[n] = 1 + move[m]
                if n == N * N:
                    return move[n]
                q.append(n)
        return -1