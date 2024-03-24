class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        loc = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            if not self.isSorted(words[i-1], words[i], loc):
                return False
        return True
        
    def isSorted(self, word1, word2, loc):
        for i in range(min(len(word1), len(word2))):
            if loc[word1[i]] < loc[word2[i]]:
                return True
            elif loc[word1[i]] > loc[word2[i]]:
                return False
        return False if(len(word1) > len(word2)) else True
        