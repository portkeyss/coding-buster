class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        A = [0]*1001
        for a,b,c in trips:
            A[b] += a
            A[c] -= a
        balance = 0
        for i in range(1001):
            balance += A[i]
            if balance > capacity: return False
        return True