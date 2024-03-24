class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        Q = set()
        x = 0
        l = 0
        while True:
            x = (10*x+1)%k
            l += 1
            if x==0: return l
            if x in Q: return -1
            Q.add(x)