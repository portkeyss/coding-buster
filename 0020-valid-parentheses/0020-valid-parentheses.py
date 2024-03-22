class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        for c in s[:]:
            if c not in dict.keys():
                stack.append(c)
            elif c in dict.keys() and (stack == [] or stack.pop() != dict[c]):
                return False
        return stack == []
        