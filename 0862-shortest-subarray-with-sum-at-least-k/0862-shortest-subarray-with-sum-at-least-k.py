class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        
        res = inf
        dq = deque()
        for i,p in enumerate(prefix):
            while dq and dq[0][1]<=p-k:
                res = min(res,i-dq.popleft()[0])
            while dq and dq[-1][1]>=p:
                dq.pop()
            dq.append((i,p))
        return res if res<inf else -1