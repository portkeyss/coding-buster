class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        inc = 0
        front = -1
        for a in A:
            if a < front:
                inc += front - a
            else:
                front = a
            front += 1
        return inc