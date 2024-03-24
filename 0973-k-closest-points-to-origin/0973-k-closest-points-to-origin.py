class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        hq = []
        for point in points:
            heapq.heappush(hq, (point[0]**2 + point[1]**2, point))
        ans = []
        for i in range(K):
            ans.append(heapq.heappop(hq)[1])
        return ans