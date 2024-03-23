class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        A = [0]*(n-1)+[shifts[-1]]
        for i in range(n-2,-1,-1):
            A[i] = A[i+1] + shifts[i]
        return "".join(chr((ord(c)-ord('a')+sh)%26+ord('a')) for c,sh in zip(s,A))