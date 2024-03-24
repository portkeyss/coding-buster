class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a==b: return "ab"*a
        if a>b:
            p = ["aa"]*(a-b-1)+["a"]*(2*b-a+2)#total b+1 segments
            q = ["b"]*b #total b segments
            l = [p[i]+q[i] for i in range(b)]+[p[-1]]
            return "".join(l)
        else:
            p = ["bb"]*(b-a-1)+["b"]*(2*a-b+2)#total a+1 segments
            q = ["a"]*a #total b segments
            l = [p[i]+q[i] for i in range(a)]+[p[-1]]
            return "".join(l)