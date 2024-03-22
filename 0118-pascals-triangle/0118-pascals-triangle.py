class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1]]
        for row in range(2, numRows + 1):
            l = [1]
            for i in range(1, row - 1):
                l.append(result[row-2][i-1]+result[row-2][i])       
            l.append(1)
            result.append(l)
        return result
        
        
        