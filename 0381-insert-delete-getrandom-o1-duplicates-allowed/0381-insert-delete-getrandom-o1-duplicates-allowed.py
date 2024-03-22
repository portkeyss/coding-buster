class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.position = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        ans = True
        if self.position[val]: ans = False
        self.lst.append(val)
        self.position[val].add(len(self.lst)-1)
        return ans

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.position[val]: return False
        if self.lst[-1] == val:
            self.lst.pop()
            self.position[val].remove(len(self.lst))
            return True
        i = self.position[val].pop()
        lastEntry = self.lst.pop()
        self.position[lastEntry].remove(len(self.lst))
        self.lst[i] = lastEntry
        self.position[lastEntry].add(i)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()