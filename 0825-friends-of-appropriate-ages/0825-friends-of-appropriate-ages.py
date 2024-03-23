class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        n = len(ages)
        ages.sort()
        res = 0
        for i,x in enumerate(ages):
            k = bisect.bisect_right(ages,0.5*x+7)
            p = bisect.bisect_right(ages,x)-1
            if k<n and ages[k]<=x:
                res += abs(p-k)
        return res