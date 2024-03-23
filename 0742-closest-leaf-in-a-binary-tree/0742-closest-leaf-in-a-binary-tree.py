# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = defaultdict(list)
        leaves = set()
        def explore(node):
            if node.left is None and node.right is None:
                leaves.add(node.val)
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                explore(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                explore(node.right)
        explore(root)
        q = deque()
        visited = set()
        q.append(k)
        visited.add(k)
        while q:
            n = q.popleft()
            if n in leaves:
                return n
            for m in graph[n]:
                if m not in visited:
                    q.append(m)
                    visited.add(m)