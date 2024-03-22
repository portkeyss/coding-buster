class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a==1:return 1
        A, B = dict(),dict()
        A[0], B[1] = 1, 0
        i = 1
        s, cycleLength = None, None
        while True:
            x = (A[i-1]*a)%1337
            if x in B:
                s = B[x]
                cycleLength = i-B[x]
                break
            else:
                A[i], B[x] = x, i
                i += 1
        
        b = [str(i) for i in b]
        def f(arr, mod):
            n = len(arr)
            d = len(str(mod))+1
            i = 0
            p = None
            while i<n:
                p = int("".join(arr[i:i+d]))%mod
                if p==0:
                    i += d
                else:
                    l = len(str(p))
                    i += d-l
                    arr[i:i+l] = [j for j in str(p)]
            return p
        
        y = f(b, cycleLength)
        return A[s+(y%cycleLength-s%cycleLength)%cycleLength]