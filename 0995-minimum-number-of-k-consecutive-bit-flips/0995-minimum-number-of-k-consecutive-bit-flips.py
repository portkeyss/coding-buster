class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        x = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==1 and len(q)%2==1 or nums[i]==0 and len(q)%2==0:
                if i<=n-k:
                    x += 1
                    q.append(i+k-1)
                else:
                    return -1
            if q and i==q[0]: q.popleft()
        return x