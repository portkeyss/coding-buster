class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        grumpyCustPrefix = [0]
        for i in range(n):
            grumpyCustPrefix.append(grumpyCustPrefix[-1]+customers[i]*grumpy[i])
        maxGrumpy = 0
        for i in range(n+1-minutes):
            maxGrumpy = max(maxGrumpy, grumpyCustPrefix[i+minutes]-grumpyCustPrefix[i])
        return sum(customers)-grumpyCustPrefix[n]+maxGrumpy