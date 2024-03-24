class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        rows = set()
        cols = set()
        points = blocked+[source,target]
        ds = [[1,0],[0,1],[-1,0],[0,-1]]
        for a,b in points:
            rows.add(a)
            cols.add(b)
            for dx,dy in ds:
                if 0<=a+dx<1000000:
                    rows.add(a+dx)
                if 0<=a-dx<1000000:
                    rows.add(a-dx)
                if 0<=b+dy<1000000:
                    cols.add(b+dy)
                if 0<=b-dy<1000000:
                    cols.add(b-dy)
        rows = sorted(rows)
        cols = sorted(cols)
        compressedRow = dict()
        compressedCol = dict()
        for i,r in enumerate(rows):
            compressedRow[r] = i
        for j,c in enumerate(cols):
            compressedCol[c] = j
        
        m = len(rows)+1 if rows[-1]<999999 else len(rows)
        n = len(cols)+1 if cols[-1]<999999 else len(cols)
        
        points = list(map(lambda x:(compressedRow[x[0]], compressedCol[x[1]]), points))
        source, target = points[-2], points[-1]
        deadends = set(points[:-1])
        def dfs(pt):
            if pt==target:
                return True
            for dx,dy in ds:
                x,y = pt[0]+dx, pt[1]+dy
                if 0<=x<m and 0<=y<n and (x,y) not in deadends:
                    deadends.add((x,y))
                    if dfs((x,y)): return True
            return False
        return dfs(source)