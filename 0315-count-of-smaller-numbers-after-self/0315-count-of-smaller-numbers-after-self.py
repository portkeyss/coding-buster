from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sl = SortedList()
        A = [0]*n
        for i in range(n-1,-1,-1):
            j = sl.bisect_left(nums[i])
            A[i] = j
            sl.add(nums[i])
        return A    