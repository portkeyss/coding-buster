class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ct = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                j += 1
            if (j - i) % k == 0: #ignore this character and go to next distinct character
                i = j
                continue
            if not ct or ct[-1][0] != s[i]: # push into ct stack
                ct.append([s[i], (j-i)%k])
            else: # merge into previous top element in stack unless they happen to form k multiples
                n = (j-i + ct[-1][1]) % k
                if n == 0:
                    ct.pop()
                else:
                    ct[-1][1] = n
            i = j
        sb = []
        for p in ct:
            sb.extend([p[0]]*p[1])
        return "".join(sb)