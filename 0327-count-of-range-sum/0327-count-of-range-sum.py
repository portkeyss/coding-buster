from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        sl.add(0)
        sm = 0
        res = 0
        for num in nums:
            sm += num
            p = sl.bisect_right(sm-lower)-1
            k = sl.bisect_left(sm-upper)
            res += p-k+1
            sl.add(sm)     
        return res