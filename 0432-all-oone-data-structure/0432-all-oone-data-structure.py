class Node:
    def __init__(self, val, prev=None, nxt=None):
        self.keys = set()
        self.val = val
        self.prev = prev
        self.nxt = nxt
        
class DoubleLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def add(self, node, p): #insert node right after p
        if self.head is None:
            self.head = self.tail = node
        elif p is None:
            node.nxt = self.head
            self.head.prev = node
            self.head = node
        else:
            q = p.nxt
            p.nxt = node
            node.prev = p
            node.nxt = q
            if q: q.prev = node
            else:
                self.tail = node
        
        
    def remove(self, node):
        p, q = node.prev, node.nxt
        if p: p.nxt = q
        if q: q.prev = p
        if node == self.head: self.head = q
        if node == self.tail: self.tail = p
        del node
        
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict() #map a key to a node in double linked list
        self.dll = DoubleLinkedList()
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.dic:
            if self.dll.head is None or self.dll.head.val > 1:
                node = Node(1)
                node.keys.add(key)
                self.dll.add(node, None)
                self.dic[key] = node
            else:
                self.dll.head.keys.add(key)
                self.dic[key] = self.dll.head
        else:
            node = self.dic[key]
            node.keys.remove(key)
            if node.nxt is None or node.nxt.val > node.val+1:  
                newNode = Node(node.val+1)
                newNode.keys.add(key)
                self.dll.add(newNode,node)
                self.dic[key] = newNode
            else:
                node.nxt.keys.add(key)
                self.dic[key] = node.nxt
            if len(node.keys) == 0:
                self.dll.remove(node)

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        node = self.dic[key]
        node.keys.remove(key)
        if node.val == 1:
            self.dic.pop(key)
        elif node.prev is None or node.prev.val < node.val-1:
            newNode = Node(node.val-1)
            newNode.keys.add(key)
            self.dll.add(newNode, node.prev)
            self.dic[key] = newNode
        else:
            node.prev.keys.add(key)
            self.dic[key] = node.prev   
        if len(node.keys) == 0:
            self.dll.remove(node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if self.dll.tail is None: return ""
        return next(iter(self.dll.tail.keys))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.dll.head is None: return ""
        return next(iter(self.dll.head.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()