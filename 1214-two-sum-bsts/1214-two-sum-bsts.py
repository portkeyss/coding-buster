# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def inorder(node, arr):
            if node is None:
                return
            inorder(node.left, arr)
            arr.add(node.val)
            inorder(node.right, arr)
        
        arr1 = set()
        arr2 = set()
        inorder(root1, arr1)
        inorder(root2, arr2)
        for n in arr1:
            if target - n in arr2:
                return True
        return False