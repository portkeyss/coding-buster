class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count1 = defaultdict(lambda:0)
        for c in "balloon":
            count1[c] += 1
        count2 = defaultdict(lambda:0)
        unique_set = set(list("balloon"))
        for c in text:
            if c in unique_set:
                count2[c] += 1
        res = float('inf')
        for c in unique_set:
            if count2[c] == 0:
                return 0
            else:
                res = min(res, count2[c]//count1[c])
        return res