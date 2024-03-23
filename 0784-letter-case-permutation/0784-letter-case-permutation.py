class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        A = [""]
        for c in s:
            B = []
            if c.isnumeric():
                for a in A:
                    B.append(a+c)
            else:
                for a in A:
                    B.append(a+c.lower())
                    B.append(a+c.upper())
            A = B
        return A