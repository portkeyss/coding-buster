class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        A = [0]*(n+2)
        for a,b,c in bookings:
            A[a] += c
            A[b+1] -= c
        
        res = []
        balance = 0
        for i in range(1,n+1):
            balance += A[i]
            res.append(balance)
        return res