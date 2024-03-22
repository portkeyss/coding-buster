class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c2i = dict()
        for i,c in enumerate(s):
            c2i[c] = i
        stack = []
        stackSet = set()
        for i,c in enumerate(s):
            if c in stackSet: continue
            while stack and stack[-1]>c and c2i[stack[-1]]>i:
                stackSet.remove(stack.pop())
            stack.append(c)
            stackSet.add(c)
        return "".join(stack)