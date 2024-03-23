class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minA = m
        minB = n
        for op in ops:
            minA = min(minA, op[0])
            minB = min(minB, op[1])
        return minA * minB