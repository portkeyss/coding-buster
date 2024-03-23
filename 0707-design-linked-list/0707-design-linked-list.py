class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        i = 0
        node = self.head
        while i < index:
            node = node[2]
            i += 1
        return node[0]
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = [val, None, self.head]
        if self.head:
            self.head[1] = node
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = [val, self.tail, None]
        if self.tail:
            self.tail[2] = node
        self.tail = node
        if self.head is None:
            self.head = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size: return
        if index == 0: self.addAtHead(val)
        elif index == self.size: self.addAtTail(val)
        else:
            i = 0
            node = self.head
            while i < index-1:
                node = node[2]
                i += 1
            newNode = [val, node, node[2]]
            node[2][1] = newNode
            node[2] = newNode
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size: return
        if index == 0:
            self.head = self.head[2]
            if self.head is None:
                self.tail = None
            else:
                self.head[1] = None
        elif index == self.size-1:
            self.tail = self.tail[1]
            if self.tail is None:
                self.head = None
            else:
                self.tail[2] = None
        else:
            i = 0
            node = self.head
            while i < index-1:
                node = node[2]
                i += 1
            node[2] = node[2][2]
            if node[2]:
                node[2][1] = node
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)