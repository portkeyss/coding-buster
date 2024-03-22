# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        prev_level = [root]
        result = [[root.val]]
        while len(prev_level) > 0:
            cur_level = []
            cur_level_vals = []
            for node in prev_level:
                if node.left:
                    cur_level.append(node.left)
                    cur_level_vals.append(node.left.val)
                if node.right:
                    cur_level.append(node.right)
                    cur_level_vals.append(node.right.val)   
            if(len(cur_level_vals) > 0):
                result.append(cur_level_vals)
            prev_level = cur_level
            
        result.reverse()
        return result