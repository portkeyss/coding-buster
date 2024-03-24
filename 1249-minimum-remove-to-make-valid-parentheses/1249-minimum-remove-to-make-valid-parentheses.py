class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        # two passes solution
        # 1) left to right, remove unmatched right parenthesis
        # 2) right to left, remove unmatched left parentesis
        # the key insight is that we store '(' in a stack, if anytime a ')' is encounterd, we pop a '(' in the stack, if the stack is empty, it means that ')' must be redundant. The second pass get rid of all redundant left parenthesis
        
        #first pass, left to right
        temp1 = []
        leftCount = 0
        for c in s:
            if c == '(':
                leftCount += 1
            elif c == ')':
                if leftCount == 0:
                    continue #remove this right parenthesis
                else:
                    leftCount -= 1
            temp1.append(c)
            
        #second pass, right to left
        temp2 = []
        rightCount = 0
        for c in reversed(temp1):
            if c == ')':
                rightCount += 1
            elif c == '(':
                if rightCount == 0:
                    continue #remove this left parenthesis
                else:
                    rightCount -= 1
            temp2.append(c)
        return "".join(reversed(temp2))
        
        
        
        
        