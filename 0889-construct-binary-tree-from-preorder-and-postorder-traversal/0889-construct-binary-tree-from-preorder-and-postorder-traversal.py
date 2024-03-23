# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        postIdx = dict((x,i) for i,x in enumerate(post))
        root = TreeNode(pre[0])
        stack = []
        stack.append(root)
        for i in range(1,len(pre)):
            while postIdx[pre[i]] > postIdx[stack[-1].val]:
                stack.pop()
            t = TreeNode(pre[i])
            if stack[-1].left is None:
                stack[-1].left = t
            else:
                stack[-1].right = t
            stack.append(t)
        return root