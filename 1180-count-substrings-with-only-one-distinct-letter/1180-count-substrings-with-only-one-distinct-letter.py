class Solution:
    def countLetters(self, S: str) -> int:
        m = len(S)
        i = 0
        cnt = 0
        while i < m:
            j = i
            while j < m and S[j] == S[i]:
                j += 1
            cnt += (j - i)*(j - i + 1)//2
            i = j
        return cnt