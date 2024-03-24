class Solution:
    def expand(self, s: str) -> List[str]:
        cur = [""]
        inBlock = False
        hq = []
        for c in s[::-1]:
            if c == "}":
                inBlock = True
            elif c == "{":
                p = []
                while hq:
                    w = heapq.heappop(hq)
                    for l in cur:
                        p.append(w+l)
                cur = p
                inBlock = False
            elif c == ",":
                continue
            else:
                if inBlock:
                    heapq.heappush(hq,c)
                else:
                    p = []
                    for l in cur:
                        p.append(c+l)
                    cur = p
        return cur