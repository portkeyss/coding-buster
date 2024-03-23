class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0]*10001
        for n in nums:
            count[n] += 1
        avoid = 0
        take = 0
        prev = None
        for i in range(1,10001):
            if count[i] == 0: continue
            if prev == i-1:
                avoid, take = max(avoid, take), avoid + count[i]*i
            else:
                avoid, take = max(avoid, take), max(avoid, take) + count[i]*i
            prev = i
        return max(avoid, take)