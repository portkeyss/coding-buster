class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == "(":
                stack.append([])
            elif c == ")":
                stack[-2] += stack[-1][::-1]
                stack.pop()
            else:
                stack[-1].append(c)
        return "".join(stack[0])