class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        if stones[-1]-stones[0]==n-1: return[0,0]
        high = max(stones[n-1]-stones[1]-n+2, stones[n-2]-stones[0]-n+2)
        if stones[-1]-stones[0]==n: return [1,high]
        low = high
        i = 0
        for j in range(n):
            while stones[j]-stones[i]>=n: i+=1
            if j-i+1==n-1 and stones[j]-stones[i]==n-2:
                return [2,high]
            else:
                low = min(low,n-(j-i+1))
        return [low,high]