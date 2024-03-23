from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def findMedian(sortedL, k):
            if k % 2 == 1:
                return sortedL[k//2]
            else:
                return (sortedL[k//2-1] + sortedL[k//2])/2
        sl = SortedList(nums[:k])
        ans = [findMedian(sl,k)]
        for i in range(k, len(nums)):
            sl.remove(nums[i-k])
            sl.add(nums[i])
            ans.append(findMedian(sl,k))
        return ans