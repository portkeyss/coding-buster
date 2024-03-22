# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        self.A = deque()
        self.B = deque()
        def inorder(node):
            if node.left:
                inorder(node.left)
            if node.val<=target:
                self.A.append(node.val)
                if len(self.A)>k:
                    self.A.popleft()
            else:
                if len(self.A)+len(self.B)<k:
                    self.B.append(node.val)
                else:
                    if self.A:
                        if target-self.A[0]<node.val-target: return
                        else:
                            self.A.popleft()
                            self.B.append(node.val)
                    else:
                        return
            if node.right:
                inorder(node.right)
        inorder(root)
        return list(self.A)+list(self.B)