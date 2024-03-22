class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        buffer = []
        available = [True]*(n+1)
        for i in range(1,n):        
            for j in range(1,n+1):
                if not available[j]: continue
                segmentSize = math.factorial(n-i)
                if segmentSize<k:
                    k -= segmentSize
                else:
                    buffer.append(str(j))
                    available[j] = False
                    break
        for j in range(1,n+1):
            if available[j]:
                buffer.append(str(j))
                break
        return "".join(buffer)