class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start==end: return 0
        bank = set(bank)
        bank.discard(start)
        if end not in bank: return -1  
        
        def neighbor(x,y):
            return sum(m!=n for m,n in zip(x,y))==1
        q = [start]
        d = 0
        while q:
            d += 1
            t = []
            for a in q:
                toDelete = []
                for b in bank:
                    if neighbor(a,b):
                        if b == end: return d
                        t.append(b)
                        toDelete.append(b)
                for e in toDelete:
                    bank.remove(e)
            q = t   
        return -1