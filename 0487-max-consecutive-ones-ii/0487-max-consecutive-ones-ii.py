class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        unflipped = 0 #current longest ones if no zero is flipped
        flipped = 0 #current longest ones if a zero is flipped
        res = 0
        for n in nums:
            if n == 0: 
                flipped = unflipped+1
                unflipped = 0
            else:
                unflipped += 1
                flipped += 1
            res = max(res, unflipped, flipped)
        return res