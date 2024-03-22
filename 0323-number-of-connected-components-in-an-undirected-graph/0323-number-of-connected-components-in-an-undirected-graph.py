class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            edge.sort()
            graph[edge[1]].append(edge[0])
        connect = {}      
        for i in range(n):
            toMerge = set()
            for j in graph[i]:
                for k, nodes in connect.items():
                    if j in nodes:
                        toMerge.add(k)
                        break
            newSet = set()
            newSet.add(i)
            for k in toMerge:
                newSet |= connect[k]
                connect.pop(k)
            connect[i] = newSet
        return len(connect)