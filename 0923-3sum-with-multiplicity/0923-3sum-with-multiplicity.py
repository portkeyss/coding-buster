class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        oneSums = Counter()
        twoSums = Counter()
        res = 0
        for x in arr:
            if target-x in twoSums:
                res += twoSums[target-x]
            for y in oneSums:
                twoSums[x+y] += oneSums[y]
            oneSums[x] += 1
        return res%(10**9+7)