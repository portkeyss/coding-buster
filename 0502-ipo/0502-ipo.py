class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #In every step, greedily pick the couple with largest possible profits existing captial range
        cp = deque(sorted((c,p) for c,p in zip(capital,profits)))
        v = w
        hq = []
        while k>0:
            while cp and v>=cp[0][0]:
                heapq.heappush(hq,-cp.popleft()[1])
            if hq:
                v += -heapq.heappop(hq)
                k -= 1
            else:
                break
        return v