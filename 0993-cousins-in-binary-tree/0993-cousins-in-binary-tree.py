# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        #BFS
        if root is None:
            return False
        q = deque()
        depth = {}
        q.append(root)
        depth[root.val] = 0
        level = None # if one of the [x,y] is known
        while q:
            node = q.popleft()
            if node.val in [x,y]:
                if level is None:
                    level = depth[node.val]
                else:
                    return level == depth[node.val]
            if node.left and node.right and node.left.val in [x,y] and node.right.val in [x,y]:
                    return False
            if node.left:
                depth[node.left.val] = depth[node.val] + 1
                q.append(node.left)
            if node.right:
                depth[node.right.val] = depth[node.val] + 1
                q.append(node.right)