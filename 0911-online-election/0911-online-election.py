class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winner = []
        curMax = 0
        votes = Counter()
        for p,t in zip(persons,times):
            votes[p] += 1
            if votes[p]>=curMax:
                self.winner.append([t,p])
                curMax = votes[p]
        
    def q(self, t: int) -> int:
        k = bisect.bisect(self.winner, [t+1])-1
        return self.winner[k][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)