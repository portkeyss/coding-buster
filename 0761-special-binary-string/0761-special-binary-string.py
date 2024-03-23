class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        stack = [[]]
        s = "1"+s+"0"
        for c in s:
            if c == "1":
                stack.append([])
            else:
                a = "".join(["1"]+sorted(stack.pop(), key=lambda x:list(x), reverse=True)+["0"])
                stack[-1].append(a)
        return stack.pop()[0][1:-1]