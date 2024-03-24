from threading import Lock, Semaphore
class DiningPhilosophers:
    
    def __init__(self):
        self.locks = [Lock() for _ in range(5)]
        self.semaphore = Semaphore(4)

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        leftFork = philosopher
        rightFork = (philosopher+4)%5
        with self.semaphore:
            self.locks[leftFork].acquire()
            pickLeftFork()
            self.locks[rightFork].acquire()
            pickRightFork()
            eat()
            putLeftFork()
            self.locks[leftFork].release()
            putRightFork()
            self.locks[rightFork].release()