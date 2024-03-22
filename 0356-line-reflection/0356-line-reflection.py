class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points.sort(key=lambda x: (x[1], x[0]))
        
        #remove duplicated values
        m = n = 1
        while m < len(points):
            if points[m][0] != points[m-1][0] or points[m][1] != points[m-1][1]:
                points[n][0] = points[m][0]
                points[n][1] = points[m][1]
                n += 1
            m += 1
        
        i = j = 0
        s = None #a placeholder to be filled once and only once
        while i < n:
            while j < n and points[i][1] == points[j][1]:
                j += 1
            start, end = i, j - 1
            if s is None:
                s = points[start][0] + points[end][0]
            while start <= end and points[start][0] + points[end][0] == s:
                start += 1
                end -= 1
            if start <= end:
                return False
            i = j
        return True
                