class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        connections = set(map(tuple, map(sorted,connections)))
        rank = [-2]*n #rank is the depth of the node being visited.
        
        def dfs(node, depth): 
            if rank[node] >= 0: #the node is already visited
                return rank[node]
            rank[node] = depth
            minDepthEncountered = rank[node]
            for nei in graph[node]:
                if rank[nei] == depth - 1:
                    continue
                d = dfs(nei, depth+1)
                if d <= depth:
                    connections.discard(tuple(sorted((node,nei))))
                minDepthEncountered = min(minDepthEncountered, d)
            
            return minDepthEncountered
            
        dfs(0,0)
        return list(connections)