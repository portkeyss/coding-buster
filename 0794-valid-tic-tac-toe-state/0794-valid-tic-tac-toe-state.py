class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        l = [set(), set()]
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    l[0].add((i,j))
                elif board[i][j] == "O":
                    l[1].add((i,j))
        if len(l[0])-len(l[1]) < 0 or len(l[0])-len(l[1]) > 1:
            return False
        triggerRow= [[0]*3 for _ in range(2)]
        triggerCol = [[0]*3 for _ in range(2)]
        triggerDiag = [0]*2
        triggerDiagPerp = [0]*2
        def f(player):
            if not l[player]: return True
            ans = False
            
            for (i,j) in l[player].copy():
                validStep = True
                l[player].remove((i,j))
                triggerRow[player][i] += 1
                if triggerRow[player][i] == 3: validStep = False
                triggerCol[player][j]+=1
                if triggerCol[player][j] == 3: validStep = False
                if i == j:
                    triggerDiag[player] += 1
                    if triggerDiag[player] == 3: validStep = False
                if i + j == 2:
                    triggerDiagPerp[player] += 1
                    if triggerDiagPerp[player] == 3: validStep = False
                
                if validStep:
                    if f(1-player): ans = True
                elif not l[0] and not l[1]:
                    ans = True
                
                l[player].add((i,j))
                triggerRow[player][i] -= 1
                triggerCol[player][j] -= 1
                if i == j:
                    triggerDiag[player] -= 1
                if i + j == 2:
                    triggerDiagPerp[player] -= 1
            
                if ans: break
                
            return ans
        return f(0)