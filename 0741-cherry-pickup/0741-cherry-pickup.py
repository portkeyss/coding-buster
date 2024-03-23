class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)        
        def traverse(r1, c1, r2,memo):
            c2 = r1+c1-r2
            if r1 == n-1 and c1 == n-1 and r2 == n-1:
                return grid[r1][c1]
            if r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if memo[r1][c1][r2] is not None:
                return memo[r1][c1][r2]
            ans = grid[r1][c1] + (r1!=r2) * grid[r2][c2]
            ans += max(traverse(r1+1, c1, r2+1, memo), traverse(r1+1, c1, r2, memo),traverse(r1, c1+1, r2+1, memo),traverse(r1, c1+1, r2, memo))
            memo[r1][c1][r2] = ans
            return ans
        memo = [[[None]*n for _1 in range(n)] for _2 in range(n)]
        return max(0,traverse(0,0,0,memo))