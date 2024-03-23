class Solution:
    def findIntegers(self, n: int) -> int:
        bit = 0
        while (1<<bit)<=n+1:
            bit += 1
        #let g[i] to be the such numbers of form 0000XXXX, where the bit before first X is the i'th bit
        g = [0]*bit
        g[0] = 1
        g[1] = 2
        for i in range(2,bit):
            g[i] = g[i-1]+g[i-2]
        
        ans = 0
        prevFilled = False
        for i in range(bit-1,-1,-1):
            if (1<<i)&(n+1):
                ans += g[i]
                if prevFilled: break
                prevFilled = True
            else:
                prevFilled = False
        return ans