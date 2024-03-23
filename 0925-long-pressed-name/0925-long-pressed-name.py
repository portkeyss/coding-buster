class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def count(word):
            l = []
            for i in range(len(word)):
                if i==0 or word[i]!=word[i-1]:
                    l.append([word[i],1])
                else:
                    l[-1][1] += 1
            return l
        A, B = count(name), count(typed)
        if len(A) != len(B): return False
        for i in range(len(A)):
            if A[i][0]!=B[i][0] or A[i][1]>B[i][1]: return False
        return True