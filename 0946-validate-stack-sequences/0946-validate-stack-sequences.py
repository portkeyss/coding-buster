class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        j = 0
        for a in pushed:
            stack.append(a)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            
        return stack == []