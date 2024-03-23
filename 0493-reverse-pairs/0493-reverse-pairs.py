from sortedcontainers import SortedList
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sl = SortedList()
        ans = 0
        for n in nums:
            i = sl.bisect_right(2 * n)
            ans += len(sl) - i
            sl.add(n)
        return ans