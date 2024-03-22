class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        standardDict = {} # map standard string to its list of shiftd strings
        for string in strings:
            standardStr = str([chr((ord(c)- ord(string[0]) + ord('a')) % 26) for c in string])
            standardDict.setdefault(standardStr,[]).append(string)
        return standardDict.values()