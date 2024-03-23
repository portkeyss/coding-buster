class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter = Counter()
        for word in words2:
            counter2 = Counter(word)
            counter|=counter2
        res = []
        for word in words1:
            counter1 = Counter(word)
            if counter1&counter==counter:
                res.append(word)
        return res