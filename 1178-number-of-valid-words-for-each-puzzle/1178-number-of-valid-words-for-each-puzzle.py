class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        count = Counter()
        for w in words:
            m = 0
            for c in w:
                m |= 1<<(ord(c)-ord('a'))
            count[m] += 1
        res = []
        for p in puzzles:
            mask = 0
            for c in p:
                mask |= 1<<(ord(c)-ord('a'))
            submask = mask
            x = 0
            while submask:
                if submask & (1<<(ord(p[0])-ord('a'))):
                    x += count[submask]
                submask = (submask-1)&mask
            res.append(x)
        return res