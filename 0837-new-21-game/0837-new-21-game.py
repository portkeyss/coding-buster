class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k+maxPts: return 1
        #let pr[x] be the probabilty of position x having been visited
        pr = [1]+[0]*n
        s = 1 # given the previous window with size min(maxPts, all previous points), s is sum over all the probabilities of points before k
        for i in range(1,n+1):
            pr[i] = s/maxPts
            if i-maxPts >= 0:
                s -= pr[i-maxPts]
            if i < k:
                s += pr[i]
        return sum(pr[k:])