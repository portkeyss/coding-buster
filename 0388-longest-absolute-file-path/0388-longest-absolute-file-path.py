class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        ans = 0
        stack = [] # [level,length] is stored in stack
        for line in lines:
            i = 0
            while i < len(line)-1 and line[i:i+1] == '\t':
                i += 1
            level = i
            length = len(line)-i      
            while stack and level <= stack[-1][0]:
                stack.pop()
            absoluteLength = stack[-1][1]+1+length if stack else length
            if '.' in line:
                ans = max(ans, absoluteLength)
            else:
                stack.append([level,absoluteLength])   
        return ans       