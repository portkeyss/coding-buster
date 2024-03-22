class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        n = sum(p>=0){(s_p - 'A' + 1) * 26**p}
        Note that s_p - 'A' + 1 runs from 1 to 26 and therefore if s_p = 'Z', then this term is divisible by 26, and this poses a problem if one uses n%26 and n/26 to seperate the first term from others. Observing that
        n = (s_0  - 'A') + 1 + sum(p>=1){(s_p - 'A' + 1) * 26**p}
        n - 1 = (s_0  - 'A') + sum(p>=1){(s_p - 'A' + 1) * 26**p}
        Now the 1st term  is  from 0 to 25, using (n-1)%26, we get S_0 - 'A', and
        (n - 1)/26 = sum(p>=1){(s_p - 'A' + 1) * 26**(p-1)}
                    = sum(q>=0){(s_(q+1) - 'A' + 1) * 26**(q)}
        which is exactly an expression for n in the next level of iteration
        that explains why we have (n-1) treatment in this algorithm
        """ 
        res = ""
        while n:
            res = chr((n-1) % 26 + ord('A')) + res
            n = (n-1)/26
        return res