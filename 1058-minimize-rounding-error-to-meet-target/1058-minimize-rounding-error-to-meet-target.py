class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        A = []
        for p in prices:
            p = float(p)
            f,c = floor(p), ceil(p)
            if f<c:
                A.append(p-floor(p))
            target -= f
        A.sort()
        if target < 0 or target>len(A): return "-1"
        res = (target-sum(A[len(A)-target:]))+sum(A[:len(A)-target])
        return "{:.3f}".format(res)