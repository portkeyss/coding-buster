class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-0.5+sqrt(0.25+2*n))