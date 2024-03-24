class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        m,n = len(arr1), len(arr2)
        dp = {-1:0}
        for x in arr1:
            tmp = defaultdict(lambda:inf)
            for y in dp:
                if y<x:
                    tmp[x] = min(tmp[x],dp[y])
                i = bisect_right(arr2,y)
                if i<n:
                    tmp[arr2[i]] = min(tmp[arr2[i]],dp[y]+1)
            dp = tmp
        return min(dp.values()) if dp else -1