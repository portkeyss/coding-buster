class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = deque()
        dq.appendleft(deck.pop())
        while deck:
            dq.appendleft(dq.pop())
            dq.appendleft(deck.pop())
        return list(dq)