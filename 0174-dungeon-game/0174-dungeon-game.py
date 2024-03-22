class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        
        @lru_cache(None)
        def minHealth(r,c):
            if r==m-1 and c==n-1:
                return 1 if dungeon[r][c]>=0 else 1-dungeon[r][c]
            minNext = min(minHealth(r+1,c) if r+1<m else inf, minHealth(r,c+1) if c+1<n else inf)
            return max(1, minNext-dungeon[r][c])

        return minHealth(0,0)