class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])        
        while True:
            S = set()
            for i in range(m):
                k = 0
                for j in range(n):
                    if board[i][j] != 0 and board[i][j] == board[i][k]:
                        if j - k + 1 == 3:
                            S.update([(i,p) for p in range(k,j+1)])
                        elif j - k + 1 > 3:
                            S.add((i,j))
                    else:
                        k = j
            for j in range(n):
                l = 0
                for i in range(m):
                    if board[i][j] != 0 and board[i][j] == board[l][j]:
                        if i - l + 1 == 3:
                            S.update([(q,j) for q in range(l, i+1)])
                        elif i - l + 1 > 3:
                            S.add((i,j))
                    else:
                        l = i
            if not S:
                return board
            for j in range(n):
                k = m-1
                for i in range(m-1, -1, -1):
                    if (i,j) in S:
                        continue
                    board[k][j] = board[i][j]
                    k -= 1
                while k > -1:
                    board[k][j] = 0
                    k -= 1
            
                
            