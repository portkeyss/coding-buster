# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if s == "":
            return None
        helper = TreeNode()
        stack = []
        stack.append(helper)
        i = -1
        while i < len(s):
            if i < 0 or s[i] == "(":
                j = i+1
                while j < len(s) and s[j] not in "()":
                    j += 1
                value = int(s[i+1:j])
                parent = stack[-1]
                newNode = TreeNode(value)
                if parent.left is None:
                    parent.left = newNode
                else:
                    parent.right = newNode
                stack.append(newNode)
                i = j
            else:
                stack.pop()
                i += 1
        return helper.left