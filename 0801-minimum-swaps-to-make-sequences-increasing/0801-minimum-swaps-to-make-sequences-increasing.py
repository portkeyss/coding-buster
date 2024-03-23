class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        stay, swap = 0, 1
        for i in range(1, len(A)):
            stayNew, swapNew = float('inf'), float('inf')
            if A[i] > A[i-1] and B[i] > B[i-1]:
                stayNew = min(stayNew, stay)
                swapNew = min(swapNew, swap+1)
            if A[i] > B[i-1] and B[i] > A[i-1]:
                stayNew = min(stayNew, swap)
                swapNew = min(swapNew, stay+1)
            stay, swap = stayNew, swapNew
        return min(stay, swap)