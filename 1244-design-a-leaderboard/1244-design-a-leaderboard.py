from sortedcontainers import SortedList
class Leaderboard:

    def __init__(self):
        self.board = {}
        self.sl = SortedList()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId in self.board:
            self.sl.remove(self.board[playerId])
            self.board[playerId] += score
        else:
            self.board[playerId] = score
        self.sl.add(self.board[playerId])

    def top(self, K: int) -> int:
        return sum(self.sl[-K:])

    def reset(self, playerId: int) -> None:
        score = self.board[playerId]
        self.board.pop(playerId)
        self.sl.remove(score)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)