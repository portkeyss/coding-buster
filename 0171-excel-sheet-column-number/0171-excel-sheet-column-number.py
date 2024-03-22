class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        p = 0
        for i in range(len(s) - 1, -1, -1):
            res += (ord(s[i]) - ord('A') + 1) * 26**p
            p += 1
        return res
            
        