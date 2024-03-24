class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper+lower:
            return []
        ans = [[0]*len(colsum) for _ in range(2)]
        for j,p in enumerate(colsum):
            if p == 2:
                ans[0][j] = 1
                upper -= 1
                if upper < 0:
                    return []
                ans[1][j] = 1
                lower -= 1
                if lower < 0:
                    return []
        for j,p in enumerate(colsum):
            if p == 1:
                if upper > 0:
                    ans[0][j] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][j] = 1
                    lower -= 1
        return ans