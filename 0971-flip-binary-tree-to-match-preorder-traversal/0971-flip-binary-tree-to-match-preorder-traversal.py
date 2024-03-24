# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        n = len(voyage)
        pos = {v:i for i,v in enumerate(voyage)}
        A = dict()
        def elements(node):
            if node is None: return set()
            A[node.val] = set([node.val])|elements(node.left)|elements(node.right)
            return A[node.val]
        
        def check(node):
            elements = A[node.val]
            l =  voyage[pos[node.val]:pos[node.val]+len(A[node.val])]
            for p in l:
                if p not in elements: return False
            return True
            
        def f(node):
            if not check(node): return False
            if not node.left and not node.right:
                return True
            if node.left and not node.right:
                i = pos[node.val]+1
                return i<n and node.left.val==voyage[i] and f(node.left)
            elif not node.left and node.right:
                i = pos[node.val]+1
                return i<n and node.right.val==voyage[i] and f(node.right)
            else:
                i = pos[node.val]+1
                if i<n and node.left.val==voyage[i]:
                    return f(node.left) and f(node.right)
                elif i<n and node.right.val==voyage[i]:
                    res.append(node.val)
                    return f(node.left) and f(node.right)
                else:
                    return False
        
        elements(root)
        res = []
        flag = f(root)
        return res if flag else [-1]          