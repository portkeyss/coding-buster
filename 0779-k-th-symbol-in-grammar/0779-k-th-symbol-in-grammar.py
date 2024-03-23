class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def f(m,q):
            if m==1: return 0
            p = f(m-1, (q+1)//2)
            if p==0:
                if q%2==1: return 0
                else: return 1
            else:
                if q%2==1: return 1
                else: return 0 
        return f(n,k)