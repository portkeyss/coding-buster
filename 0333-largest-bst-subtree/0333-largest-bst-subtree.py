# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if root is None: return 0
        def dfs(node):
            if node.left is None and node.right is None:
                return (True, 1, node.val, node.val)
            if node.left is None:
                rightBST, rightCount, rightMin, rightMax = dfs(node.right)
                if rightBST and node.val < rightMin:
                    self.lgst = max(self.lgst, 1+rightCount)
                    return (True, 1+rightCount,node.val, rightMax)
                else:
                    return (False, None, None, None)
            if node.right is None:
                leftBST, leftCount, leftMin, leftMax = dfs(node.left)
                if leftBST and node.val > leftMax:
                    self.lgst = max(self.lgst, 1+leftCount)
                    return (True, 1+leftCount, leftMin, node.val)
                else:
                    return (False, None, None, None)
            leftBST, leftCount, leftMin, leftMax = dfs(node.left)
            rightBST, rightCount, rightMin, rightMax = dfs(node.right)
            if leftBST and rightBST and leftMax < node.val < rightMin:
                self.lgst = max(self.lgst, 1+leftCount+rightCount)
                return (True, 1+leftCount+rightCount, leftMin, rightMax)
            else:
                return (False, None, None, None) #only the 1st entry matters if it is not a BST
            
        self.lgst = 1
        dfs(root)
        return self.lgst   