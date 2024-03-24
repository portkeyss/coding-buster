class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        cnt = collections.Counter(A)
        hq = []
        for k,freq in cnt.items():
            if freq == 1:
                heapq.heappush(hq, -k)
        if hq:
            return -hq[0]
        else:
            return -1