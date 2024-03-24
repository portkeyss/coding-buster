class Solution:
    def encode(self, num: int) -> str:
        if num == 0: return ""
        bit = 1
        while 2**(bit+1)-2 < num: bit += 1
        seq = num - (2**bit-1) #sequence number in the current number of with digit number "bit", counting from 0
        buffer = []
        while seq:
            buffer.append(str(seq%2))
            seq //= 2
        while len(buffer) < bit:
            buffer.append("0")
        return "".join(buffer[::-1])