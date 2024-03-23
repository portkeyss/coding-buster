class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i = bisect.bisect(arr,x)
        l, r = i-1, i
        while l >= 0 and r < len(arr) and r-l-1 < k:
            if abs(arr[l]-x) <= abs(arr[r]-x):
                l -= 1
            else:
                r += 1
        if l < 0:
            return arr[:k]
        if r >= len(arr):
            return arr[-k:]
        return arr[l+1:r]