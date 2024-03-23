# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root.left is None and root.right is None: return [root.val]
        def findBoundary(node, left=True):
            if left:
                if node.left is None: return []
                node = node.left
            else:
                if node.right is None: return []
                node = node.right
            ans = []
            while node.left or node.right:
                ans.append(node.val)
                if left:
                    node = node.left if node.left else node.right
                else:
                    node = node.right if node.right else node.left
            return ans if left else ans[::-1]
        def dfs(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        leftBoundary = findBoundary(root, True)
        rightBoundary = findBoundary(root, False)
        leaves = []
        dfs(root)
        return [root.val] + leftBoundary + leaves + rightBoundary