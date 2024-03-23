class Solution:
    def toHex(self, num: int) -> str:
        if num==0: return "0"
        positive = True if num>0 else False
        if not positive:
            num = (1<<32)-abs(num)
        A = []
        while num>0:
            p = num%16
            x = str(p) if p<10 else chr(p-10+ord('a'))
            A.append(x)
            num //= 16
        return "".join(A[::-1])