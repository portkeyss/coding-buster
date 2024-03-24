class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        dp = [[i] for i in range(10)]
        A = [i for i in range(10)]
        bit = len(str(high))
        for b in range(2,bit+1):
            t = [[] for _ in range(10)]
            if b!= bit:
                t[0] = dp[1].copy()
            for i in range(1,9):
                for n in dp[i-1]:
                    t[i].append(i*10**(b-1)+n)
                for n in dp[i+1]:
                    t[i].append(i*10**(b-1)+n)
            for n in dp[8]:
                t[9].append(9*10**(b-1)+n)
            A.extend([x for d in range(1,10) for x in t[d]])
            dp = t
        i = bisect.bisect_left(A,low)
        j = bisect.bisect(A,high)
        return A[i:j]