class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        if cols < max(len(w) for w in sentence):
            return 0
        effectiveUnit = " ".join(sentence)+" "
        unitLen = len(effectiveUnit)
        cursor = 0 
        for _ in range(rows):
            cursor += cols-1
            if effectiveUnit[cursor%unitLen] == " ":
                cursor += 1
            elif effectiveUnit[(cursor+1)%unitLen] == " ":
                cursor += 2
            else:
                while effectiveUnit[cursor%unitLen] != " ":
                    cursor -= 1
                cursor += 1
        return cursor//unitLen