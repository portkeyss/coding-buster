class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = j = 0
        ans = 0
        holes = 0
        while j < len(A):
            if A[j] == 0:
                holes += 1
            while holes > K:
                if A[i] == 0:
                    holes -= 1
                i += 1
            ans = max(ans, j-i+1)
            j += 1
        return ans