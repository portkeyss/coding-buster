class Solution:
    def commonChars(self, A: List[str]) -> List[str]:        
        m = collections.Counter(A[0])
        for a in A[1:]:
            m &= collections.Counter(a)
        return list(m.elements())