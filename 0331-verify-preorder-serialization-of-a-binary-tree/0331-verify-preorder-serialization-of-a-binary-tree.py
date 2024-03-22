class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder=="#": return True
        preorder = preorder.split(",")
        if preorder[0]=="#": return False
        stack = [0] # states of node in stack, 0 means only value assigned, 1 means left child filled, 2 means right child filled
        for s in preorder[1:]:
            if stack:
                stack[-1] += 1
                if stack[-1]==2:
                    stack.pop()
                if s!="#":
                    stack.append(0)
            else:
                return False
        return not stack