class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums
        self.k = k
        heapq.heapify(self.l)
        while len(self.l) > self.k:
            heapq.heappop(self.l)

    def add(self, val: int) -> int:
        if len(self.l) < self.k:
            heapq.heappush(self.l, val)
        elif val > self.l[0]:
            heapq.heapreplace(self.l,val)
        return self.l[0]
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)