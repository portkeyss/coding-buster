class Solution:
    def lastRemaining(self, n: int) -> int:
        def f(start, end, reverse, length, delta):
            if length == 1:
                return start
            newLength = length//2
            newDelta = delta * 2
            if reverse is False:
                start += delta
                end = start + newDelta*(newLength-1)
                reverse = True
            else:
                end -= delta
                start = end - newDelta*(newLength-1)
                reverse = False
            return f(start, end, reverse, newLength, newDelta)
        return f(1, n,False, n, 1)