class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1:[1]}
        def f(n):
            if n in memo:
                return memo[n]
            odds = f((n+1)//2)
            evens = f(n//2)
            memo[n] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[n]
        return f(N)