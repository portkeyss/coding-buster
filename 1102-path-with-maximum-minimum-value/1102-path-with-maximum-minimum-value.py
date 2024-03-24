class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        candidates = set()
        
        for i in range(R):
            for j in range(C):
                if A[i][j] <= min(A[0][0], A[R-1][C-1]):
                    candidates.add(A[i][j])
        candidates = list(candidates)
        candidates.sort()
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def isValid(val, i, j, seen):
            if i == R-1 and j == C-1:
                return True
            if seen[i][j]:
                return False   
            if A[i][j] < val:  
                return False
            seen[i][j] = 1
            for d in directions:
                x, y = i+d[0], j+d[1]
                if 0<=x<R and 0<=y<C and isValid(val, x, y, seen):
                    return True
            return False
                   
        l, r = 0, len(candidates)-1
        while l < r:
            mid = ceil((l+r)/2)
            seen = [[0 for c in range(C)] for _ in range(R)]
            if isValid(candidates[mid], 0, 0, seen):
                l = mid
            else:
                r = mid - 1
        return candidates[r]