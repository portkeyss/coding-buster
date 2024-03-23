# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.buffer = []
        def preorder(node):      
            self.buffer.append(str(node.val))
            if not node.left and not node.right: return
            self.buffer.append("(")
            if node.left:
                preorder(node.left)
            self.buffer.append(")")
            if node.right:
                self.buffer.append("(")
                preorder(node.right)
                self.buffer.append(")")
        
        preorder(root)
        return "".join(self.buffer)