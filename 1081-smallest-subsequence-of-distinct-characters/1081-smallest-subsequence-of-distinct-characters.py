class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        stackSet = set()
        lastOccur = {c:i for i,c in enumerate(s)}
        for i,c in enumerate(s):
            if c in stackSet: continue
            while stack and stack[-1]>c and lastOccur[stack[-1]]>i:
                stackSet.remove(stack.pop())
            stack.append(c)
            stackSet.add(c)
        return "".join(stack)