# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = None
        self.q = deque()
        if root:
            self.root = root
            self.q.append(root)
            while self.q:
                node = self.q[0]
                if node.left:
                    self.q.append(node.left)
                if node.right:
                    self.q.append(node.right)
                    self.q.popleft()
                else:
                    break
                
    def insert(self, val: int) -> int:
        node = TreeNode(val)
        parent = None
        if self.root is None:
            self.root=node
        elif self.q[0].left is None:
            self.q[0].left = node
            parent = self.q[0].val
        else:
            self.q[0].right = node
            parent = self.q[0].val
            self.q.popleft()
        self.q.append(node)
        return parent

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()