class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        l, r = 0, n-1
        while seats[l] == 0:
            l += 1
        while seats[r] == 0:
            r -= 1
        res = max(l, n-1-r)
        zeros = 0
        for i in range(l+1,r+1):
            if seats[i] == 0:
                zeros += 1
            else:
                res = max(res, (zeros+1)//2)
                zeros = 0
        return res