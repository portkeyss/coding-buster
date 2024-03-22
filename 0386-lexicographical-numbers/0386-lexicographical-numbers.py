class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = [i for i in range(1,n+1)]
        l = list(map(str, l))
        l.sort()
        l = list(map(int, l))
        return l