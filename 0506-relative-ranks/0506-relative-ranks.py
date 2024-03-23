class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        rank = sorted(list(i for i in range(n)),key=lambda x: -score[x])
        res = [None]*n
        for i,j in enumerate(rank):
            if i==0: res[j]="Gold Medal"
            elif i==1: res[j] = "Silver Medal"
            elif i==2: res[j] = "Bronze Medal"
            else: res[j] = str(i+1)
        return res