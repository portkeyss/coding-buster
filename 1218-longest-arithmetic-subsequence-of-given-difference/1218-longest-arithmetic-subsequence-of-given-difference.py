class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        A = defaultdict(lambda:0)
        for i in arr:
            A[i] = max(A[i], A[i-difference]+1)
        return max(A.values())  