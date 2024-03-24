class Solution:
    def baseNeg2(self, n: int) -> str:
        if n==0: return "0"
        buffer = []
        while n:
            buffer.append(n+2*ceil(n/(-2)))
            n = ceil(n/(-2))
        return "".join(str(d) for d in buffer[::-1])