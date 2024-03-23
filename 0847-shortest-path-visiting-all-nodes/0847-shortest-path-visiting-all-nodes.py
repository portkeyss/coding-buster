class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        cache = dict()
        
        def f(node, mask): #given mask, how many steps can we get here. Note that we are thinking backward because hereby state is unique(no bother thinking about the order of nodes traversed)
            if mask&(mask-1)==0: return 0
            state = (node, mask)
            if state in cache: return cache[state]
            cache[state] = inf
            for nei in graph[node]:
                if mask&(1<<nei)!=0: #note that we are thinking backward, if nei is shown at the mask that it is not visited yet, we should not dip into it at this point
                    unvisited = 1+f(nei,mask^(1<<node))
                    visited = 1+f(nei,mask)
                    cache[state] = min(cache[state], unvisited, visited)       
            return cache[state]
        
        return min(f(i,(1<<n)-1) for i in range(n))