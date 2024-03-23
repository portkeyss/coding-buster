class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [-1] *k
        self.k = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.k
        self.q[self.tail] = value
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.q[self.head] = -1
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.k
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.q[self.head] if not self.isEmpty() else -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1 and self.tail == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.head == (self.tail + 1) % self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()