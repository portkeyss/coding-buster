class MyHashSet:

    def __init__(self):
        self.hs = BSTree()

    def add(self, key: int) -> None:
        self.hs.insert(self.hs.root, key)

    def remove(self, key: int) -> None:
        self.hs.remove(self.hs.root, key)

    def contains(self, key: int) -> bool:
        return self.hs.contains(self.hs.root, key)

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTree:

    def __init__(self):
        self.root = None

    def contains(self, root, val):
        if root is None: return False
        if root is None: return
        if root.val==val: return True
        if root.val<val: return self.contains(root.right, val)
        return self.contains(root.left,val)

    def insert(self, root, val):
        if root is None: 
            root = TreeNode(val)
            if self.root is None:
                self.root = root
        elif root.val<val:
            root.right = self.insert(root.right, val)
        elif root.val>val:
            root.left = self.insert(root.left,val)
        return root

    def remove(self, root, val):
        if root is None: return None
        elif root.val<val:
            root.right = self.remove(root.right, val)
            return root
        elif root.val>val:
            root.left = self.remove(root.left, val)
            return root
        else:
            if not root.left and not root.right:
                if self.root==root:
                    self.root = None
                return None
            if root.left is None:
                return root.right
            prev = root.left
            t = None
            while prev.right:
                t = prev
                prev = prev.right
            root.val = prev.val
            if prev==root.left: root.left=prev.left
            else:
                t.right = prev.left
            return root
                



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)