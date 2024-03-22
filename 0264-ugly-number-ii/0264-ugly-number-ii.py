class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2=i3=i5=0
        A = [1]
        for i in range(1,n):
            x = min(2*A[i2], 3*A[i3], 5*A[i5])
            A.append(x)
            if x==2*A[i2]: i2+=1
            if x==3*A[i3]: i3+=1
            if x==5*A[i5]: i5+=1
        return A[n-1]