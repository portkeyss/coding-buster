class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        A = defaultdict(list)
        for i,k in enumerate(groupSizes):
            if A[k] and len(A[k][-1])<k: A[k][-1].append(i)
            else: A[k].append([i])
        return [a for l in A.values() for a in l]