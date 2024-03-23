class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        dic = defaultdict(set)
        for p in similarPairs:
            dic[p[0]].add(p[1])
            dic[p[1]].add(p[0])
        for w1,w2 in zip(sentence1,sentence2):
            if w1 == w2 or w2 in dic[w1]:
                continue
            else:
                return False
        return True 