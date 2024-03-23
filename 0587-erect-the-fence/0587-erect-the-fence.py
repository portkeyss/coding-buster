class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees)<=3: return trees
        epsilon = 0.0000001
        trees.sort()
        start = 0
        helper = [trees[start][0],trees[start][1]+1]
        fences = [0]
        cur = start
        candidates = set(range(len(trees)))
        def dot(vec1, vec2):
            return vec1[0]*vec2[0]+vec1[1]*vec2[1]
        
        def distSqr(vec1, vec2):
            vec = (vec1[0]-vec2[0], vec1[1]-vec2[1])
            return dot(vec,vec)
        
        def cosine(t0, t1, t2):
            v1 = (t1[0]-t0[0], t1[1]-t0[1])
            v2 = (t2[0]-t0[0], t2[1]-t0[1])
            return dot(v1,v2)/sqrt(dot(v1,v1)*dot(v2,v2))
            
        while True:
            minCosine = inf
            cur = None
            for i in candidates:
                if i==start and len(fences)==1: continue
                t0 = trees[fences[-1]]
                t1 = helper if len(fences)==1 else trees[fences[-2]]
                t2 = trees[i]
                cos = cosine(t0, t1, t2)
                if cos<minCosine-epsilon or abs(cos-minCosine)<epsilon and distSqr(trees[i], trees[fences[-1]])<distSqr(trees[cur], trees[fences[-1]]):
                    minCosine = cos
                    cur = i        
            if cur==start:
                break
            else:
                fences.append(cur)
                candidates.remove(cur)
        return [trees[i] for i in fences]    