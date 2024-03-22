class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        unfilled = []
        availableRow = [set(j for j in "123456789") for _ in range(9)]
        availableCol = [set(j for j in "123456789") for _ in range(9)]
        availableSub =[[set(j for j in "123456789") for _ in range(3)] for __ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    unfilled.append([i,j])
                else:
                    availableRow[i].remove(board[i][j])
                    availableCol[j].remove(board[i][j])
                    availableSub[i//3][j//3].remove(board[i][j])
        def f():
            if not unfilled:
                return True
            i,j = unfilled.pop()
            available = availableRow[i]&availableCol[j]&availableSub[i//3][j//3]
            for c in available:
                availableRow[i].remove(c)
                availableCol[j].remove(c)
                availableSub[i//3][j//3].remove(c)
                board[i][j] = c
                if f(): return True
                board[i][j] = "."
                availableRow[i].add(c)
                availableCol[j].add(c)
                availableSub[i//3][j//3].add(c)
            unfilled.append((i,j))
            return False

        f()