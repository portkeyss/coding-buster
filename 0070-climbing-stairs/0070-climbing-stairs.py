class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        ways_prev_prev = 1
        ways_prev = 2
        for i in range(2,n):
            ways = ways_prev + ways_prev_prev
            ways_prev_prev = ways_prev
            ways_prev = ways
        return ways