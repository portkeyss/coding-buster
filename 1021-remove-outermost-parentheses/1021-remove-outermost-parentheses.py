class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        buffer = []
        n = len(s)
        i = 1
        balance = 0
        for j in range(n):
            if s[j]=="(": balance += 1
            else: balance -= 1
            if balance==0:
                buffer.append(s[i:j])
                i = j+2
        return "".join(buffer)