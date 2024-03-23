class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        buffer = []
        n = len(s)
        j = n-1
        for i in range(n):
            if s[i].isalpha():
                while not s[j].isalpha():
                    j -= 1
                buffer.append(s[j])
                j -= 1
            else:
                buffer.append(s[i])
        return "".join(buffer)