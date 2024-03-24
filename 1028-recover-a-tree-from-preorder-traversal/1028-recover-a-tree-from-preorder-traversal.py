# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)
        A = []
        while i<n:
            d = 0
            while i<n and traversal[i]=="-":
                d += 1
                i += 1
            num = 0
            while i <n and traversal[i].isnumeric():
                num = num*10+int(traversal[i])
                i += 1
            A.append([d,num])
        helper = TreeNode(-1)
        stack.append([helper,-1])
        for d,num in A:
            node = TreeNode(num)
            if d>stack[-1][1]:
                stack[-1][0].left = node
            else:
                while d<=stack[-1][1]: stack.pop()
                stack[-1][0].right = node
            stack.append([node,d])
        return helper.left