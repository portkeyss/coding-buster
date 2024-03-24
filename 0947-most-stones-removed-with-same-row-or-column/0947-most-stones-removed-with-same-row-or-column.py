class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = defaultdict(set)
        col = defaultdict(set)
        for x,y in stones:
            row[x].add(y)
            col[y].add(x)
        
        def dfs(a,b):
            if b in row[a]:
                row[a].remove(b)
                col[b].remove(a)
                for y in row[a].copy():
                    dfs(a,y)
                for x in col[b].copy():
                    dfs(x,b)
        
        components = 0
        for x,y in stones:
            if y not in row[x]: continue
            dfs(x,y)
            components += 1
        return len(stones)-components