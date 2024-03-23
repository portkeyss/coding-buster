class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        A = defaultdict(list)
        for n in nums:
            if n-1 in A:
                length=heapq.heappop(A[n-1])
                if not A[n-1]:
                    A.pop(n-1)
                heapq.heappush(A[n], length+1)
            else:
                heapq.heappush(A[n], 1)
        for a in A.values():
            if a[0]<3: return False
        return True