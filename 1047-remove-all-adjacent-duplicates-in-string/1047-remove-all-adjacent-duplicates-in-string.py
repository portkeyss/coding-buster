class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if not stack or stack[-1] != ch:
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)