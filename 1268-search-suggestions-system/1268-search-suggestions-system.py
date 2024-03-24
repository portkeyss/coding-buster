class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = [[] for _ in range(len(searchWord))]
        for prod in products:
            i = 0
            while i < min(len(prod), len(searchWord)) and prod[i] == searchWord[i]:
                if len(res[i]) < 3:
                    res[i].append(prod)
                i += 1
        return res