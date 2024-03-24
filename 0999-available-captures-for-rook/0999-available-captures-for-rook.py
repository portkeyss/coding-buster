class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m = 8
        pos = None
        for i in range(m):
            for j in range(m):
                if board[i][j]=="R":
                    pos = (i,j)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        res = 0
        for dx,dy in directions:
            x, y = pos[0]+dx,pos[1]+dy
            while 0<=x<m and 0<=y<m:
                if board[x][y]=="B":break
                elif board[x][y]=="p":
                    res += 1
                    break
                else:
                    x += dx
                    y += dy
        return res