class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9+7
        def findMaxSum(a):
            mx = 0
            cur = 0
            for x in a:
                cur += x
                mx = max(mx, cur)
                if cur < 0: cur = 0
            return mx
        
        mx1 = findMaxSum(arr)
        res = 0
        if k==1: res = mx1
        else:
            sm = sum(arr)
            prefixMax = 0
            cur = 0
            for c in arr:
                cur += c
                prefixMax = max(prefixMax, cur)
            postfixMax = 0
            cur = 0
            for c in arr[::-1]:
                cur += c
                postfixMax = max(postfixMax, cur)
            if sm <= 0:
                res = max(mx1,prefixMax+postfixMax)
            else:
                res = max(mx1,prefixMax+postfixMax+(k-2)*sm)
        return res%mod   