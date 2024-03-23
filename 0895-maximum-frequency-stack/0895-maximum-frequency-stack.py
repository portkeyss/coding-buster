class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.groupbyfreq = defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.groupbyfreq[self.freq[x]].append(x)
        self.maxfreq = max(self.maxfreq, self.freq[x])

    def pop(self) -> int:
        x = self.groupbyfreq[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.groupbyfreq[self.maxfreq]:
            self.maxfreq -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()