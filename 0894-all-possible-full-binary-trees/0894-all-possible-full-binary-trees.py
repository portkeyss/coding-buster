# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = []
        dp.append([])
        dp.append([TreeNode()])
        for i in range(2, n+1):
            dp.append([])
            for l in range(1,i-1):
                left = dp[l]
                right = dp[i-l-1]
                if left==[] or right==[]: continue
                for a in left:
                    for b in right:
                        t = TreeNode()
                        t.left = a
                        t.right = b
                        dp[-1].append(t)
        return dp[n]