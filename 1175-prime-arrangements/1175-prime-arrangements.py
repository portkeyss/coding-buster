class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10**9+7
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        primeBits = bisect.bisect(primes,n)
        return factorial(primeBits)*factorial(n-primeBits)%mod
        