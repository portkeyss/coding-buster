class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n==1: return 1
        l = len(primes)
        hq = [[primes[0],0]]
        for _ in range(2,n):
            m,f = heapq.heappop(hq)
            if f<l-1:
                heapq.heappush(hq,(m//primes[f]*primes[f+1],(f+1)))
            heapq.heappush(hq,(m*primes[f], f))
        return hq[0][0]