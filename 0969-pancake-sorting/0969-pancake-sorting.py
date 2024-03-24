class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        mx = len(arr)
        
        def rev(a, p):
            l,r = 0, p
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1
        res = []       
        while mx > 1:
            idx = arr.index(mx)
            if idx < mx-1:          
                rev(arr, idx)
                rev(arr, mx-1)
                res.append(idx+1)
                res.append(mx)
            mx -= 1
        return res