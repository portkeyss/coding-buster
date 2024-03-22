class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ""
        res = ""
        for i in range(len(strs[0])):
            j = 1
            while j < len(strs) and i < len(strs[j]) and strs[j][i] == strs[j-1][i]:
                j += 1
            if j == len(strs):
                res += strs[0][i]
            else:
                break
        return res
        