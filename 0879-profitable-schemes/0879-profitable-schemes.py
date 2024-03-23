class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        A = Counter()
        A[(0,0)] = 1
        mod = 10**9+7
        res = 0
        for g,p in zip(group,profit):
            B = Counter()
            for a,b in A.keys():
                if a+g<=n:
                    B[(a+g,min(minProfit,b+p))] = (B[(a+g,min(minProfit,b+p))]+A[(a,b)])%mod
            A += B
        for (_,b),c in A.items():
            if b==minProfit:
                res = (res+c)%mod
        return res