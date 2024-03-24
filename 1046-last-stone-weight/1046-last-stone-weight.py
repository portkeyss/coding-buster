class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for stone in stones:
            heapq.heappush(hq, -stone)
        while True:
            if len(hq) == 0:
                return 0
            if len(hq) == 1:
                return -hq[0]
            a = - heapq.heappop(hq)
            b = - heapq.heappop(hq)
            if a > b:
                heapq.heappush(hq,-(a-b))