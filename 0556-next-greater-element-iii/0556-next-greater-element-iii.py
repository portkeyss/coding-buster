class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nlist = list(str(n))
        n = len(nlist)
        p = n - 2
        while p >= 0 and nlist[p] >= nlist[p+1]:
            p -= 1
        if p < 0:
            return -1
        q = n - 1
        while nlist[q] <= nlist[p]:
            q -= 1
        nlist[p], nlist[q] = nlist[q], nlist[p]
        l,r = p+1, n-1
        while l < r:
            nlist[l], nlist[r] = nlist[r], nlist[l]
            l += 1
            r -= 1
        res = int("".join(nlist))
        return res if res < 1<<31 else -1