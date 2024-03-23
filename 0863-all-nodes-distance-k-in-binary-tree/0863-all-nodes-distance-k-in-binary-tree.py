# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = defaultdict(list)
        def traverse(node):
            if node.left is not None:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                traverse(node.left)
            if node.right is not None:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                traverse(node.right)
        traverse(root) # build graph
        
        q = collections.deque()
        q.append(target.val)
        INFNTY = 10**10
        dist = defaultdict(lambda:INFNTY)
        dist[target.val] = 0
        res = []
        while q:
            n = q.popleft()
            if dist[n] == K:
                res.append(n)
            for nei in graph[n]:
                if dist[nei] == INFNTY:
                    q.append(nei)
                    dist[nei] = 1 + dist[n]
        return res
            