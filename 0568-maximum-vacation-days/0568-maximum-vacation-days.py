class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n,k = len(days),len(days[0])   
        dest = [[] for _ in range(n)]
        for i in range(n):
            dest[i].append(i) #it allows for staying for another week in the same city
            for j in range(n):
                if flights[i][j]==1: dest[i].append(j)
        week = 0
        A = [0]+[-inf]*(n-1)
        while week<k:
            B = [-inf]*n
            for city in range(n):
                for j in dest[city]:
                    B[j] = max(B[j],A[city]+days[j][week])
            A = B
            week += 1
        return max(A)