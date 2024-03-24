class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ops = 0
        while startValue<target:
            if target%2==0:
                ops += 1
                target //= 2
            else:
                ops += 2
                target = (target+1)//2
        return ops+startValue-target