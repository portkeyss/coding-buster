class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = defaultdict(lambda:0)
        for t in transactions:
            balance[t[0]] += t[2]
            balance[t[1]] -= t[2]
        bal = []
        for m in balance.values():
            if m != 0:
                bal.append(m)

        n = len(bal)
        def dfs(x):
            while x < n and bal[x] == 0:
                x += 1
            if x == n: return 0
            res = n
            for i in range(x+1, n):
                if bal[x] * bal[i] >= 0: continue   
                bal[i] += bal[x]  
                res = min(res, 1+dfs(x+1))
                bal[i] -= bal[x]
            return res
        
        return dfs(0)