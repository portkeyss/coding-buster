class Solution:
    def knightDialer(self, n: int) -> int:
        nextNums = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        count = [1]*10
        for _ in range(2,n+1):
            newCount = [0]*10
            for i in range(10):
                for j in nextNums[i]:
                    newCount[j] += count[i]
            count = newCount
        return sum(count)%(10**9+7)
            
        