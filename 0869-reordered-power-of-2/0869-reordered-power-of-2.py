class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        bit = len(str(n))
        counter = Counter(str(n))
        i = 0
        while True:
            if (1<<i)<10**(bit-1): i+=1
            elif (1<<i)>=10**bit:break
            else:
                if Counter(str(1<<i))==counter: return True
                i += 1
        return False