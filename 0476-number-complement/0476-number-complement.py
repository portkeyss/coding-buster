class Solution:
    def findComplement(self, num: int) -> int:
        b = 0
        while (1<<b)<=num:
            b += 1
        return ((1<<b)-1)&(~num)
        