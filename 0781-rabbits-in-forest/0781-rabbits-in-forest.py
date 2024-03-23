class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter()
        for a in answers:
            count[a+1] += 1
        res = 0
        for i,c in count.items():
            if c>0:
                res += ((c+i-1)//i)*i
        return res