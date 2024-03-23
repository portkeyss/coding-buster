class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        ct = 0
        m = ceil(math.sqrt(2 * N))
        for n in range(1,m):
            if 2 * N % n != 0:
                continue
            w = 2 * N // n
            if (n % 2 == 0 and w % 2 == 1) or (n % 2 == 1 and w % 2 == 0):
                ct += 1
        return ct
                
    