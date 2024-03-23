class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        A = [[i,j] for i in range(n) for j in range(n) if img1[i][j]==1]
        res = 0
        for x in range(-n+1,n):
            for y in range(-n+1,n):
                a = 0
                for i,j in A:
                    if 0<=i+x<n and 0<=j+y<n and img2[i+x][j+y]:
                        a += 1
                res = max(res, a)
        return res