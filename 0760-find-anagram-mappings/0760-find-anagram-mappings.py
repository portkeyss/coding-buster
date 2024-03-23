class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        ind = defaultdict(deque)
        res = []
        for i, b in enumerate(B):
            ind[b].append(i)
        for j, a in enumerate(A):
            res.append(ind[a].popleft())
        return res