class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        iters = [iter(num) for num in nums]
        hq = [(next(it),i) for i,it in enumerate(iters)]
        right = max(x for x,_ in hq)
        heapq.heapify(hq)
        ans = -10**10, 10**10
        while hq:
            left, i = heapq.heappop(hq)
            if right-left < ans[1]-ans[0]:
                ans = left, right
            nxt = next(iters[i],None)
            if nxt is None:
                return ans
            right = max(right, nxt)
            heapq.heappush(hq, (nxt,i))    