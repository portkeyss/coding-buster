class Solution:
    def confusingNumber(self, N: int) -> bool:
        s = str(N)
        rotate = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        t = []
        for c in s[::-1]:
            if c in rotate:
                t.append(rotate[c])
            else:
                return False
        return s != "".join(t)