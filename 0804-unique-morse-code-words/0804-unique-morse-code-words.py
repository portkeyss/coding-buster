class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mc = {ch:code for ch,code in zip(list("abcdefghijklmnopqrstuvwxyz"),[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        s = set()
        for w in words:
            s.add("".join(mc[ch] for ch in w))
        return len(s)