class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = arr[-1] - arr[0]
        for i in range(1, len(arr)):
            minDiff = min(minDiff, arr[i] - arr[i-1])
        res = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minDiff:
                res.append([arr[i-1], arr[i]])
        return res