class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        A = Counter()
        B = Counter()
        C = 0
        for a in arr:
            if a > 0: A[a] += 1
            elif a < 0: B[-a] += 1
            else: C += 1
        if C%2: return False
        def f(M):
            V = sorted(list(M.keys()))
            for a in V:
                if M[a] == 0: continue
                if M[2*a] < M[a]:
                    return False
                M[2*a] -= M[a]
                if M[2*a]==0: M.pop(2*a)
                M.pop(a)
            return len(M)==0
        return f(A) and f(B)