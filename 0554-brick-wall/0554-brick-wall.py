class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        A = defaultdict(lambda:0)
        n = len(wall)
        m = sum(wall[0])
        for i in range(len(wall)):
            j = 0
            for width in wall[i]:
                A[2*j] += 1
                A[2*(j+width)-1] -= 1
                j += width
        points = sorted(A.keys())
        points.pop()
        balance = 0
        res = inf
        for pt in points:
            balance += A[pt] 
            res = min(res, balance)
        return res