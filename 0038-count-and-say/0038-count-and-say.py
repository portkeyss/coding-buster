class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        st = "1"
        for i in range(1,n):
            prev_s = st
            st = ""
            m = prev_s[0]
            count = 1
            for j in range(1,len(prev_s)):
                if prev_s[j] == m:
                    count += 1
                else:
                    st += str(count) + m
                    m = prev_s[j]
                    count = 1
            st +=  str(count) + m
        return st