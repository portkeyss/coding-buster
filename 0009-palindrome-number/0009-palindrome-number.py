class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = x
        reverse = 0
        while y != 0:
            reverse = 10 * reverse + y % 10
            y /= 10
        return reverse == x