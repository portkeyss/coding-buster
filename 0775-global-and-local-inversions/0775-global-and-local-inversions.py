class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        floor = math.inf
        for i in range(len(nums)-1,1,-1):
            floor = min(floor, nums[i])
            if floor < nums[i-2]:
                return False
        return True