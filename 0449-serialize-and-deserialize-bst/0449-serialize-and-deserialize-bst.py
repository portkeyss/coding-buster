# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if root is None: return ""
        buffer = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node is None:
                buffer.append("n")
                buffer.append("#")
            else:
                buffer.append(str(node.val))
                buffer.append("#")
                q.append(node.left)
                q.append(node.right)
        while buffer and buffer[-1] in ["n", "#"]:
            buffer.pop() #remove trailing "#" and "n"
        return "".join(buffer)
            

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == "": return None
        buffer = data.split("#")
        placeholder = TreeNode(-1)
        q = deque()
        root = None
        for s in buffer:
            node = None if s=="n" else TreeNode(int(s))
            if not q:
                q.append(node)
                root = node
            elif q[0].left is None:
                q[0].left = node if node else placeholder
                if node:
                    q.append(node)
            else:
                q[0].right = node
                if q[0].left == placeholder:
                    q[0].left = None
                if node:
                    q.append(node)
                q.popleft()
        return root
       

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans