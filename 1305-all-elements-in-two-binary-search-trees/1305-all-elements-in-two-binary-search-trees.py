# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, l):
            if node is None: return
            inorder(node.left, l)
            l.append(node.val)
            inorder(node.right, l)
        
        l1 = []
        l2 = []
        inorder(root1,l1)
        inorder(root2,l2)
        
        i,j = 0,0
        res = []
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        if i<len(l1): res += l1[i:]
        elif j<len(l2): res += l2[j:]
        return res