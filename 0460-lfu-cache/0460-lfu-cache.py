class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vals = dict()
        self.counter = dict()
        self.countToKeys = defaultdict(dict) # ordered set is needed, but since python does not support ordered set, ordered dict becomes the choice. And since python dict are ordered in key by construction, it is used here
        self.min = None
        
    def get(self, key: int) -> int:
        if key not in self.vals: return -1
        count = self.counter[key]
        self.counter[key] += 1
        self.countToKeys[count].pop(key)
        self.countToKeys[count+1][key] = True
        if self.min == count and len(self.countToKeys[count]) == 0:
            self.min += 1
        return self.vals[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return 
        if key in self.vals:  
            count = self.counter[key]
            self.counter[key] += 1
            self.countToKeys[count].pop(key)
            self.countToKeys[count+1][key] = True
            if self.min == count and len(self.countToKeys[count]) == 0:
                self.min += 1
        else:
            if len(self.vals) == self.capacity:
                k, _ = next(iter(self.countToKeys[self.min].items()))
                self.vals.pop(k)
                self.countToKeys[self.min].pop(k)
                self.counter.pop(k)
            self.counter[key] = 1
            self.min = 1
            self.countToKeys[1][key] = True
        self.vals[key] = value   
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)