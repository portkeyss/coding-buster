class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent = dict()
        for c,p in zip(pid,ppid):
            parent[c] = p
        
        survive = set()
        destroy = set([kill])
        i = parent[kill]
        while i != 0:
            survive.add(i)
            i = parent[i]
        
        for a in pid:
            if a in survive or a in destroy: continue
            candidates = set()
            while a not in survive and a not in destroy:
                candidates.add(a)
                a = parent[a]
            if a in survive:
                survive.update(candidates)
            else:
                destroy.update(candidates)
        return list(destroy)