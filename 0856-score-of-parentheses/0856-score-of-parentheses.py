class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        stack.append([False,0]) #S[0] always is "("
        for i in range(1,len(S)):
            if S[i] == "(": 
                if stack[-1][0] is False:
                    stack.append([False, 0])
                else:
                    stack[-1][0] = False
            else:
                if stack[-1][0] is True: #the current level is blanced, should find match in the lower level
                    stack[-2][0] = True
                    stack[-2][1] += 2*stack[-1][1]
                    stack.pop()
                else: # match should be found at the current level
                    stack[-1][0] = True
                    stack[-1][1] += 1
        return stack[0][1]