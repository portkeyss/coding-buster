class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==0: return True
        if word[0].isupper():
            return all(c.isupper() for c in word[1:]) or all(c.islower() for c in word[1:])
        else:
            return all(c.islower() for c in word[1:])