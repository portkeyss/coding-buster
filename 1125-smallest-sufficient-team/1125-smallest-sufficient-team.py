class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n = len(req_skills)
        r2i = dict()
        for i,x in enumerate(req_skills):
            r2i[x] = i
        
        m2t = {0:[]}
        for i,p in enumerate(people):
            mask = 0
            for x in p:
                mask |= 1<<(r2i[x])
            t = m2t.copy()
            for m in t:
                if m|mask not in m2t or len(t[m])+1<len(m2t[m|mask]):
                    m2t[m|mask] = t[m]+[i]
        return m2t[(1<<n)-1]    