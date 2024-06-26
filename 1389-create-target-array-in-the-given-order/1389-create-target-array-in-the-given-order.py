class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i,n in zip(index, nums):
            ans.insert(i,n)
        return ans