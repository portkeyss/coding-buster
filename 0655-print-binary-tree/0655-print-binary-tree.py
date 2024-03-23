# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        m = 0
        q = [root]
        while q:
            t = []
            for x in q:
                if x.left:
                    t.append(x.left)
                if x.right:
                    t.append(x.right)
            q = t
            m += 1 
        n = (1<<m)-1
        res = [[""]*n for _ in range(m)]
        q = [[root,(n-1)//2]]
        r = 0
        while q:
            t = []
            for x,c in q:
                res[r][c] = str(x.val)
                if x.left:
                    t.append([x.left, c-(1<<(m-r-2))])
                if x.right:
                    t.append([x.right,c+(1<<(m-r-2))])
            q = t
            r += 1
        return res