class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = float('-inf')
        for n in preorder:
            if n < low:
                return False
            while stack and stack[-1] < n:
                low = stack.pop()
            stack.append(n)
        return True