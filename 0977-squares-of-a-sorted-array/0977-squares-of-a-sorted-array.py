class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        p = 0
        while p < len(A) and A[p] <= 0:
            p += 1
        i = p
        j = p - 1
        
        res = []
        while i < len(A) and j >= 0:
            if A[i]**2 >= A[j]**2:
                res.append(A[j]**2)
                j -= 1
            else:
                res.append(A[i]**2)
                i += 1
        while i < len(A):
            res.append(A[i]**2)
            i += 1
        while j >= 0:
            res.append(A[j]**2)
            j -= 1
        return res