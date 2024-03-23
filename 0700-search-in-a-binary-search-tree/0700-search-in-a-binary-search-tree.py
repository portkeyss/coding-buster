# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val==val: return root
        stack = [iter([root])]
        while stack:
            x = next(stack[-1],None)
            if x is None:
                stack.pop()
            else:
                if x.val==val: return x
                if not x.left and not x.right:
                    continue
                l = []
                if x.left: l.append(x.left)
                if x.right: l.append(x.right)
                stack.append(iter(l))
        return None       