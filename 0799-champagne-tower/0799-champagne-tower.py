class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if query_row == 0:
            return poured if poured <= 1 else 1
        last = [poured]
        for i in range(1, query_row+1):
            l = [0]*(i+1)
            for j in range(len(last)):
                if last[j] > 1:
                    l[j] += 0.5*(last[j]-1)
                    l[j+1] += 0.5*(last[j]-1)
            last = l
        return 1 if last[query_glass]>1 else last[query_glass]