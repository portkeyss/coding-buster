class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.row_occupancy = [[0]*n for i in range(2)]
        self.col_occupancy = [[0]*n for i in range(2)]
        self.cross_occupancy = [0,0]
        self.diag_occupancy = [0,0]

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        self.row_occupancy[player-1][row] += 1
        if self.row_occupancy[player-1][row] == self.n:
            return player
        self.col_occupancy[player-1][col] += 1
        if self.col_occupancy[player-1][col] == self.n:
            return player
        if row + col == self.n -1:
            self.cross_occupancy[player-1] += 1
            if self.cross_occupancy[player-1] == self.n:
                return player
        if row == col:
            self.diag_occupancy[player-1] += 1
            if self.diag_occupancy[player-1] == self.n:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)