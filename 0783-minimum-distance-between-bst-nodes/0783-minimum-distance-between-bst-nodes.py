# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        lst = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            lst.append(node.val)
            inorder(node.right)
        
        inorder(root)
        res = lst[1]-lst[0]
        for i in range(2,len(lst)):
            res = min(res, lst[i]-lst[i-1])
        return res