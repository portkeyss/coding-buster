# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        def f(node, isLeftNode):
            if not node.left and not node.right:
                if isLeftNode:
                    return node.val
                else:
                    return 0
            ans = 0
            if node.left:
                ans += f(node.left, True)
            if node.right:
                ans += f(node.right, False)
            return ans
        return f(root, False)         