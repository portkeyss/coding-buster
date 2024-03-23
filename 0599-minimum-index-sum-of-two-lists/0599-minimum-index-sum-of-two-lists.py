class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        A = {x:i for i,x in enumerate(list1)}
        B = []
        idxSum = inf
        for i,x in enumerate(list2):
            if x not in A or A[x]+i>idxSum: continue
            if A[x]+i<idxSum:
                B = [x]
                idxSum = A[x]+i
            else:
                B.append(x)
        return B