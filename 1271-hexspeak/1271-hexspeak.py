class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        hexDec = []
        while num > 0:
            residual = num % 16
            if 1 < residual < 10:
                return "ERROR"
            if residual == 0:
                residual = "O"
            elif residual == 1:
                residual = "I"
            else:
                residual = chr(residual-10+ord('A'))
            hexDec.append(residual)
            num //= 16
        return "".join(hexDec[::-1])
        