class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx={num:i for i,num in enumerate(arr2)}
        return sorted(arr1,key=lambda x: (idx[x] if x in idx else inf,x))