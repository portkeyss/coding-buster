from threading import Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.locks = [Lock() for _ in range(4)]
        for lock in self.locks[:-1]:
            lock.acquire()
    
    def resetLock(self):
        self.i += 1
        if self.i%15 == 0:self.locks[0].release()
        elif self.i%3 == 0:self.locks[1].release()
        elif self.i%5 == 0:self.locks[2].release()
        else:self.locks[3].release()
    
    def releaseAllLocks(self):
        for lock in self.locks:
            if lock.locked(): lock.release()
                
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.locks[1].acquire()
            if self.i > self.n: 
                self.releaseAllLocks()
                return
            printFizz()
            self.resetLock()
        

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.locks[2].acquire()
            if self.i > self.n: 
                self.releaseAllLocks()
                return
            printBuzz()
            self.resetLock()
        

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.locks[0].acquire()
            if self.i > self.n: 
                self.releaseAllLocks()
                return
            printFizzBuzz()
            self.resetLock()
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.locks[3].acquire()
            if self.i > self.n: 
                self.releaseAllLocks()
                return
            printNumber(self.i)
            self.resetLock()