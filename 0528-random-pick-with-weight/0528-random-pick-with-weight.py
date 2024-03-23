class Solution:

    def __init__(self, w: List[int]):
        self.indices = [i for i in range(len(w))]
        totweight = sum(w)
        self.ws = [w/totweight for w in w]

    def pickIndex(self) -> int:
        return random.choices(population = self.indices, 
                      weights = self.ws,
                     k = 1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()