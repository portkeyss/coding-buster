class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a, b = len(str(low)), len(str(high))
        s = "123456789"
        res = []
        for length in range(a,b+1):
            for i in range(10-length):
                t = int(s[i:i+length])
                if low<=t<=high: res.append(t)
        return res