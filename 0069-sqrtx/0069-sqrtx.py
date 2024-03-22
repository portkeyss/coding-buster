class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        for highest_bit in range(15, -1, -1):
            if (res + (1 << highest_bit))**2 <= x:
                res += (1 << highest_bit)
        return res
        