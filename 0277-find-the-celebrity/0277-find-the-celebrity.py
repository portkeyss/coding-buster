# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            j = 0
            while j < n:
                if i == j:
                    j += 1
                    continue
                if knows(i,j) or not knows(j,i):
                    break
                j += 1
            if j == n:
                return i
        return -1