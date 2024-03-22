class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        dividers = defaultdict(lambda:0)
        for update in updates:
            start, end, inc = update[0], update[1]+1, update[2]
            dividers[start] += inc
            dividers[end] -= inc
        A = [[point,inc] for point,inc in dividers.items()]
        A.sort(key=lambda x:x[0])
        cumSum = 0
        B = []
        for a in A:
            cumSum += a[1]
            B.append([a[0], cumSum])
        res = [0]*length
        for i in range(len(B)):
            end = B[i+1][0] if i < len(B)-1 else length
            for j in range(B[i][0], end):
                res[j] += B[i][1]
        return res  