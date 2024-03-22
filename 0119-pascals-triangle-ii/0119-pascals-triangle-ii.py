class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        l = [1]
        for r in range(1, rowIndex + 1):
            for i in range(r-1, 0, -1):
                l[i] += l[i-1]   
            l.append(1)
        return l
        