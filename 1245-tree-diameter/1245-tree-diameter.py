class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if len(edges) == 0:
            return 0
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node, parent = -1):
            if len(graph[node]) == 1 and parent != -1: #this is the condition for identifying a leaf
                return 0
            l = []
            for nei in graph[node]:
                if nei != parent:
                    heapq.heappush(l, -(1+dfs(nei, node)))         
            i = 0
            radii = []
            while l and i < 2:
                radii.append(-heapq.heappop(l))
                i += 1
            self.diameter = max(self.diameter, sum(radii))
            return radii[0]
        
        self.diameter = 0
        dfs(edges[0][0]) #this is an arbitary choice and can be replace by any other nodes thanks to the nature of undirected tree structure
        return self.diameter