class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        A = []
        s = []
        for i in range(n):
            while s and arr[s[-1]]>=arr[i]:
                s.pop()
            A.append(s[-1] if s else -1)
            s.append(i)
        B = []
        s = []
        for i in range(n-1,-1,-1):
            while s and arr[s[-1]]>arr[i]:
                s.pop()
            B.append(s[-1] if s else n)
            s.append(i)
        B = B[::-1]
        res = 0
        for i in range(n):
            res += arr[i]*(i-A[i])*(B[i]-i)
        return res%(10**9+7)