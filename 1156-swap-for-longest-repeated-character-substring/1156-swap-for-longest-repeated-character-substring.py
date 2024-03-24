class Solution:
    def maxRepOpt1(self, text: str) -> int:
        m = len(text)
        prev = None
        A = []
        B = Counter() #how many intervals of consecutive char are there in the text
        for ch in text:
            if ch!=prev:
                A.append([ch,1])
                B[ch] += 1
            else:
                A[-1][1] += 1
            prev = ch
        n = len(A)
        res = 0
        for i in range(n):
            if i<n-2 and A[i+1][1]==1 and A[i+2][0]==A[i][0]:
                if B[A[i][0]]>2:
                    res = max(res, A[i][1]+1+A[i+2][1])
                else:
                    res = max(res, A[i][1]+A[i+2][1])
            elif A[i][1]<m and B[A[i][0]]>1:
                res = max(res, A[i][1]+1)
            else:
                res = max(res, A[i][1])
        return res