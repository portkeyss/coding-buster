class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        root = 0 #root is arbitrarily chosen
        neighbors = [[] for _ in range(n)]
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        subtreeDistance = [0]*n
        subtreeCount = [1]*n
        def f(node, parent):
            if neighbors[node]==[parent]: return
            for nei in neighbors[node]:
                if nei!=parent:
                    f(nei,node)
                    subtreeDistance[node] += subtreeCount[nei]+subtreeDistance[nei]
                    subtreeCount[node] += subtreeCount[nei]
        f(root, -1)
        
        totDist = [0]*n
        totDist[root]=subtreeDistance[root]
        def g(node, parent):
            for nei in neighbors[node]:
                if nei!=parent:
                    totDist[nei] = totDist[node]+n-2*subtreeCount[nei]
                    g(nei,node)
        g(root,-1)
        return totDist