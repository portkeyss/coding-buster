class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        #trim outmost nodes until no more than 2 nodes are left
        nei = defaultdict(set)
        for a,b in edges:
            nei[a].add(b)
            nei[b].add(a)
        
        outer = [i for i in range(n) if len(nei[i])==1]
        nodes = set(range(n))
        while len(nodes)>2:
            t = []
            for p in outer:
                q = nei[p].pop()
                nei[q].remove(p)
                if len(nei[q])==1: t.append(q)
                nei.pop(p)
                nodes.remove(p)
            outer = t
        return list(nodes)