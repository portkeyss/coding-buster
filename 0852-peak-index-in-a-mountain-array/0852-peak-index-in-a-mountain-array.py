class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        while l+1<r:
            m = (l+r)//2
            if arr[m]<arr[m+1]:
                l = m
            elif arr[m]<arr[m-1]:
                r = m
            else:
                return m