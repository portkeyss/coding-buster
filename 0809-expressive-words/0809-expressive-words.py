class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def f(w):
            A = []
            for c in w:
                if A==[] or c!=A[-1][0]: A.append([c,1])
                else:A[-1][1] += 1
            return A
        sRep = f(s)
        res = 0
        for word in words:
            wRep = f(word)
            if len(sRep) != len(wRep): continue
            flag = True
            for i in range(len(sRep)):
                if sRep[i][0] != wRep[i][0] or sRep[i][1] < wRep[i][1] or sRep[i][1] > wRep[i][1] and sRep[i][1]==2:
                    flag = False
                    break
            if flag: res += 1
        return res    