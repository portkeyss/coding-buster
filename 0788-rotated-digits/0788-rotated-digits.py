class Solution:
    def rotatedDigits(self, n: int) -> int:
        allowed = {"0","1","8"}
        must = {"2","5","6","9"}
        res = 0
        for i in range(1,n+1):
            s = str(i)
            valid = False
            for c in s:
                if c in allowed: continue
                elif c in must: valid = True
                else:
                    valid = False
                    break
            if valid:
                res += 1
        return res