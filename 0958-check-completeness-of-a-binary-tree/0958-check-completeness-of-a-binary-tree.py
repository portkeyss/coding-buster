# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q = deque()
        q.append(root)
        end = False    
        while q:
            node = q.popleft()
            if node.left:
                if end is True:
                    return False
                q.append(node.left)
            else:
                end = True
            if node.right:
                if end is True:
                    return False
                q.append(node.right)
            else:
                end = True
        return True