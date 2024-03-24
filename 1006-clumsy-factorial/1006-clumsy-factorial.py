class Solution:
    def clumsy(self, n: int) -> int:
        x = 0
        y = n
        j = 0
        for i in range(n-1,0,-1):
            if j==0:
                y *= i   
            elif j==1:
                y = y//i if y>0 else -((-y)//i)
                x += y
                y = 0
            elif j==2:
                x += i
            else:
                y = -i
            j = (j+1)%4
        x += y
        return x 