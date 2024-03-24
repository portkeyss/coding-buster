class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0,1,1]
        for i in range(3,n+1):
            T.append(T[-3]+T[-2]+T[-1])
        return T[n]