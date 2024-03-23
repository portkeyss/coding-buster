class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for n in ops:
            if n not in "+DC":
                stack.append(int(n))
            elif n == "+":
                stack.append(stack[-2] + stack[-1])
            elif n == "D":
                stack.append(2*stack[-1])
            else:
                stack.pop()
        return sum(stack)