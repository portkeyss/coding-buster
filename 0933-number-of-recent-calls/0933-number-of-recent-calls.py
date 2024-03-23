class RecentCounter:

    def __init__(self):
        self.l = []

    def ping(self, t: int) -> int:
        self.l.append(t)
        j = bisect.bisect_left(self.l, t-3000)
        return len(self.l) - j


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)