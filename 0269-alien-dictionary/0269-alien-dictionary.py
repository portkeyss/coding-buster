class Solution:
    def alienOrder(self, words: List[str]) -> str:       
        predecessors = {}
        for w in words:
            for c in w:
                predecessors[c] = set() #initialize the map for every character and map it to an empty set
        for i in range(1, len(words)):
            k = 0
            m, n = len(words[i-1]), len(words[i])
            while k < m and k < n and words[i-1][k] == words[i][k]:
                k += 1
            if k == m and m <= n:
                continue
            if k == n and m > n:
                return ""
            predecessors[words[i][k]].add(words[i-1][k])
        
        order = []
        while predecessors:
            toDelete = []
            for w, p in predecessors.items():
                if len(p) == 0:
                    toDelete.append(w)
            if toDelete == []:
                return ""
            order.extend(toDelete)
            for w in toDelete:
                predecessors.pop(w) 
                for p in predecessors.values():
                    p.discard(w)
        return "".join(order)