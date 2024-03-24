class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x:x[2])
        parent = [-1]*(N+1) #node range from 1 to N
        
        def findRoot(node, parent):
            if parent[node] == -1:
                return node
            return findRoot(parent[node],parent)
        
        def insert(a, b, w, graph, parent):
            graph[a].append(b)
            graph[b].append(a)
            rearrangeTree(a, graph, parent)
        
        def rearrangeTree(root, graph, parent):      
            def dfs(node, prev):
                parent[node] = prev
                for m in graph[node]:
                    if m != prev:
                        dfs(m, node)
            dfs(root, -1)
                      
        graph = defaultdict(list)
        cost = 0
        edgeCount = 0
        for edge in connections:
            a, b, w = edge[0], edge[1], edge[2]
            r1, r2 = findRoot(a,parent), findRoot(b,parent)
            if r1 == r2:
                continue
            insert(a, b, w, graph, parent)
            cost += w
            edgeCount += 1
            if edgeCount == N-1:
                return cost
        return -1