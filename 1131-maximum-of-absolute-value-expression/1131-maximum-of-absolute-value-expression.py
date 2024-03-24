class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        A = [x+y+i for i,(x,y) in enumerate(zip(arr1,arr2))]
        B = [x-y+i for i,(x,y) in enumerate(zip(arr1,arr2))]
        C = [-x+y+i for i,(x,y) in enumerate(zip(arr1,arr2))]
        D = [-x-y+i for i,(x,y) in enumerate(zip(arr1,arr2))]
        return max(max(A)-min(A),max(B)-min(B), max(C)-min(C), max(D)-min(D))