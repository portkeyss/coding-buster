class Solution:
    def findPermutation(self, s: str) -> List[int]:
        res = []
        stack = []
        for k,c in enumerate(s):
            if c=="I":
                res.append(k+1)
                while stack:
                    res.append(stack.pop())
            else:
                stack.append(k+1)
        res.append(len(s)+1)
        while stack:
            res.append(stack.pop())
        return res        