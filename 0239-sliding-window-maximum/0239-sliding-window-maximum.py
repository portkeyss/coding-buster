class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        #monotonic decreasing deque
        q = deque()
        for i,h in enumerate(nums):
            if q and i-q[0]+1>k: q.popleft()
            while q and nums[q[-1]]<=h: q.pop()
            q.append(i)
            if i>=k-1: res.append(nums[q[0]])
        return res