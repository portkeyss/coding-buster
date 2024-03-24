class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evenSum = oddSum = 0 
        for p in position:
            if p%2==0:
                evenSum += 1
            else:
                oddSum += 1
        return min(evenSum, oddSum)