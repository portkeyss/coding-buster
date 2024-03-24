from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.mainLock = Lock()
        self.evenLock = Lock()
        self.evenLock.acquire()
        self.oddLock = Lock()
        self.oddLock.acquire()
            
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2*self.n):
            if i%2 == 0:
                self.mainLock.acquire()
                printNumber(0)
            elif (i-1)%4 == 0:
                self.oddLock.release()
            else:
                self.evenLock.release()
           
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2,self.n+1, 2):
            self.evenLock.acquire()
            printNumber(i)
            self.mainLock.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1, 2):
            self.oddLock.acquire()
            printNumber(i)
            self.mainLock.release()