class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        dq = deque()
        A = nums+nums
        prefix = 0
        res = -inf
        for i,x in enumerate(A):
            while dq and dq[0][0]<i-n:
                dq.popleft()
            prefix += x
            res = max(res,prefix-dq[0][1] if dq else prefix)
            while dq and dq[-1][1]>=prefix:
                dq.pop()
            dq.append((i,prefix))
        return res