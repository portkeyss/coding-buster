class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        l1 = num1.split("+")
        l2 = num2.split("+")
        a, b, c,d = int(l1[0]), int(l1[1][:-1]), int(l2[0]), int(l2[1][:-1]),
        p = a*c-b*d
        q = a*d+b*c
        return str(p)+"+"+str(q)+"i"