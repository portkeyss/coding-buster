class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = [] #record timestamps of hit
        self.count = {} #map timestamp to number of hits at this timestamp

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp in self.count:
            self.count[timestamp] += 1
        else:
            self.timestamps.append(timestamp)
            self.count[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.timestamps:
            return 0
        i = bisect.bisect_right(self.timestamps, timestamp - 300)     
        return sum([self.count[timestamp] for timestamp in self.timestamps[i:]])


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)