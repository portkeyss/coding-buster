class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(t):
            count = 0
            for c in t:
                if c=="(": count += 1
                elif c==")":
                    count -= 1
                    if count<0: return False
            return count==0

        if valid(s): return [s]
        res = []
        #BFS
        q = [s]
        visited = set([s])
        found = False
        while q:
            tmp = []
            for t in q:
                for i in range(len(t)):
                    if t[i] not in "()": continue
                    x = t[:i]+t[i+1:]                   
                    if x not in visited:
                        if valid(x):
                            res.append(x)
                            found = True
                        else:
                            tmp.append(x)
                        visited.add(x)
            if found: break
            q = tmp
        return res