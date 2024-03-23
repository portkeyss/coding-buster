class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        n = len(A)
        if len(B) != n:
            return False
        if n == 0:
            return True
        for i in range(n):
            if A == B[i:] + B[:i]:
                return True
        return False