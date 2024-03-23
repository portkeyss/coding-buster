class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        A = sorted(arr)
        s1 = s2 = 0
        res = 0
        for a, b in zip(arr,A):
            s1 += a
            s2 += b
            if s1==s2: res += 1
        return res