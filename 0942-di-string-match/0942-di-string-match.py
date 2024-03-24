class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        A = []
        mi, mx = 0, len(s)
        for c in s:
            if c=="I":
                A.append(mi)
                mi += 1
            else:
                A.append(mx)
                mx -= 1
        A.append(mi) #both mi and mx are okay, since mi==mx
        return A