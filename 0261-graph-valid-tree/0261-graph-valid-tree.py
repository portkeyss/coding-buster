class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges == []:
            return n < 2
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        A = set()
        def isTree(node, parent=-1):
            A.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei in A:
                    return False
                if not isTree(nei, node):
                    return False
            return True
        return isTree(edges[0][0]) and len(A) == n