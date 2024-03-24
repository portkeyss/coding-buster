class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        cur = 0
        for i in range(n):
            if i==0 or arr[i]==arr[i-1]:
                cur = 1
            elif arr[i]<arr[i-1]:
                if i>=2 and arr[i-1]>arr[i-2]:
                    cur += 1
                else:
                    cur = 2
            else:
                if i>=2 and arr[i-1]<arr[i-2]:
                    cur += 1
                else:
                    cur = 2
            res = max(res, cur)
        return res