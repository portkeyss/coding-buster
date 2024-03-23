class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = defaultdict(list) # map content to path
        for i, s in enumerate(paths):
            l = s.split()
            for j, file in enumerate(l):
                m = file.split("(")
                if len(m) == 1:
                    continue
                name, content = m[0], m[1][:-1]
                p = "/".join([l[0],name])
                mp[content].append(p)
        
        res = []
        for content, lst in mp.items():
            if len(lst) >= 2:
                res.append(lst)
        return res