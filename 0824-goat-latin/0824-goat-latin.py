class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = set(c for c in "aAeEiIoOuU")
        return " ".join([w+"ma"+"a"*(i+1) if w[0] in vowel else w[1:]+w[0]+"ma"+"a"*(i+1) for i,w in enumerate(sentence.split(" "))])