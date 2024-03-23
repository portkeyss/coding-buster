class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distSqr(p,q):
            return (points[p][0]-points[q][0])**2+(points[p][1]-points[q][1])**2
        A = defaultdict(Counter)
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                ds = distSqr(i,j)
                A[i][ds] += 1
                A[j][ds] += 1
        res = 0
        for i in range(n):
            for v in A[i].values():
                res += v*(v-1)
        return res