class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        for s in stones:
            tmp = set()
            for x in dp:
                tmp.add(x+s)
                tmp.add(x-s)
            dp = tmp
        return min(abs(w) for w in dp) 