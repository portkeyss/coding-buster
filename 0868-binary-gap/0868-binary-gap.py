class Solution:
    def binaryGap(self, n: int) -> int:
        bit = int(log(n,2))+1
        prev = -1
        res = 0
        for i in range(bit+1):
            if (1<<i)&n:
                if prev>=0:
                    res = max(res, i-prev)
                prev = i
        return res