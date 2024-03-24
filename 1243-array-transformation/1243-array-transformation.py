class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n<3: return arr
        while True:
            change = False
            prev = arr[0]
            for i in range(1,n-1):
                mi = min(prev,arr[i+1])
                mx = max(prev,arr[i+1])
                prev = arr[i]
                if arr[i]<mi:
                    arr[i] += 1
                    change = True
                elif arr[i]>mx:
                    arr[i] -= 1
                    change = True
            if not change:
                return arr