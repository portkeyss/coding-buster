from threading import Lock
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = deque()
        self.qlock = Lock()
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock2.acquire()

    def enqueue(self, element: int) -> None:
        self.lock1.acquire()
        with self.qlock:
            self.q.append(element)
            if len(self.q) == 1:
                self.lock2.release()
            if len(self.q) < self.capacity:
                self.lock1.release()

    def dequeue(self) -> int:
        self.lock2.acquire()
        with self.qlock:
            element = self.q.popleft()
            if len(self.q) == self.capacity-1:
                self.lock1.release()
            if len(self.q) > 0:
                self.lock2.release()
        return element

    def size(self) -> int:
        return len(self.q)