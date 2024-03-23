from heapq import heappush,heappop
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m,n = len(heightMap),len(heightMap[0])
        boundary = []
        visited = [[False]*n for _ in range(m)]
        d = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(m):
            if not visited[i][0]:
                heappush(boundary,(heightMap[i][0],i,0))
                visited[i][0] = True
            if not visited[i][n-1]:
                heappush(boundary,(heightMap[i][n-1],i,n-1))
                visited[i][n-1] = True
        for j in range(n):
            if not visited[0][j]:
                heappush(boundary,(heightMap[0][j],0,j))
                visited[0][j] = True
            if not visited[m-1][j]:
                heappush(boundary,(heightMap[m-1][j],m-1,j))
                visited[m-1][j] = True
        res = 0
        while boundary:
            h,i,j = heappop(boundary)
            for dr,dc in d:
                if 0<=i+dr<m and 0<=j+dc<n and not visited[i+dr][j+dc]:
                    if heightMap[i+dr][j+dc] < h:
                        res += h-heightMap[i+dr][j+dc]
                    heappush(boundary,(max(h,heightMap[i+dr][j+dc]),i+dr,j+dc))
                    visited[i+dr][j+dc] = True
        return res