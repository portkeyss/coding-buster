class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        #union find
        root = {x:x for x in "abcdefghijklmnopqrstuvwxyz"}
        rank = defaultdict(lambda:0)
        def union(a,b):
            r1 = findRoot(a)
            r2 = findRoot(b)
            if r1==r2: return
            if rank[r1]>rank[r2]:
                root[r2] = r1
            elif rank[r1]<rank[r2]:
                root[r1] = r2
            else:
                root[r2] = r1
                rank[r1] += 1
                
        def findRoot(a):
            if root[a]==a: return a
            root[a] = findRoot(root[a])
            return root[a]
        
        A = []
        B = []
        for equ in equations:
            x, ops, y = equ[0], equ[1:3], equ[3]
            if ops=="==":
                A.append([x,y])
            else:
                B.append([x,y])
        for x,y in A:
            union(x,y)
        for x,y in B:
            if findRoot(x)==findRoot(y): return False
        return True