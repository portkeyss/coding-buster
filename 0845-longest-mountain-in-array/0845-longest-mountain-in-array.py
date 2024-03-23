class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        uphill = False
        downhill = False #this flag is True only if this downward slope is preceeded immediately by an upward slope
        start = n #inactive starting point
        for i in range(1,n):
            if arr[i-1] < arr[i]:
                if uphill is False:
                    start = i-1
                    uphill = True
                downhill = False
            elif arr[i-1] > arr[i]:
                if uphill is True:  
                    uphill = False
                    downhill = True
                if downhill is True:
                    ans = max(ans, i-start+1)
            else:
                uphill = False
                downhill = False
        return ans