class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        dp = {}
        def chg(amount: int, i: int) -> int: # i is the starting index of the coins in the current recusive step
            if (amount, i) in dp:
                return dp[(amount, i)]
            if amount == 0:
                return 1
            if coins[i:] == []:
                return 1 if amount == 0 else 0
            
            div = amount // coins[i]
            
            ways = 0
            for n in range(div+1):
                ways += chg(amount-n*coins[i], i+1)
            dp[(amount,i)] = ways
            return ways
        
        return chg(amount, 0)