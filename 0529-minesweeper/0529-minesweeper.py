class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        directions = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        p, q = click[0], click[1]
        if board[p][q] == 'M':
            board[p][q] = 'X'
            return board
        
        def dfs(i,j):
            adjacentMines = 0
            neighbors = []
            for d in directions:
                x, y = d[0] + i, d[1] + j
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if board[x][y] in ['M','X']:
                    adjacentMines += 1
                elif board[x][y] == 'E':
                    neighbors.append([x,y])
                    
            if adjacentMines > 0:
                board[i][j] = str(adjacentMines)
                return
            board[i][j] = 'B'
            for nei in neighbors:
                dfs(nei[0],nei[1])       
         
        dfs(p,q)
        return board
                