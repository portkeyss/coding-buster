class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        start = "".join(str(x) for l in board for x in l)
        if start == "123450":
            return 0
        q = deque()
        dist = dict()
        q.append(start)
        dist[start] = 0
        while q:
            n = q.popleft()
            idx = n.index("0")
            i, j = idx//3, idx%3
            for d in directions:
                i1,j1 = i+d[0],j+d[1]
                if i1<0 or i1>=2 or j1<0 or j1>=3: continue
                idx1 = i1*3+j1
                p = list(n)
                p[idx], p[idx1] = p[idx1], p[idx]
                p = "".join(p)
                if p not in dist:
                    q.append(p)
                    dist[p] = dist[n]+1
                    if p=="123450":
                        return dist[p]
        return -1