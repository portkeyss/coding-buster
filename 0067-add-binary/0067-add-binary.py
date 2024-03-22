class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        st = ""
        while i >= 0 or j >= 0 or carry > 0:
            m = 0
            n = 0
            if i >= 0:
                m = int(a[i])
                i -= 1
            if j >= 0:
                n = int(b[j])
                j -= 1
            
            st = str((m + n + carry) % 2) + st
            carry = (m + n + carry) / 2
            
        return st