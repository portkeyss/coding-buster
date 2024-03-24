class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        i, j = 0, len(A)-1
        while i < j:
            mid = (i + j)//2
            if A[mid] < mid:
                i = mid + 1
            elif A[mid] > mid:
                j = mid - 1
            else:
                j = mid
        return i if i == j and A[i] == i else -1