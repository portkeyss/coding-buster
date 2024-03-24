class Solution:
    def divisorGame(self, N: int) -> bool:
        #dynmaical programming
        win = [False]*(N+1)
        for i in range(1,N+1):
            for x in range(1,i//2+1): # for x > i//2, i%x == 0 can never hold, this is a small improvement over th upper bound N-1
                if i % x == 0 and win[i-x] == False:
                    win[i] = True
                    break
        return win[N]