class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        pay = 0
        while len(sticks) >= 2:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            pay += x + y
            heapq.heappush(sticks, x+y)
        return pay