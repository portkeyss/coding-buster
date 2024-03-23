class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        res = 0
        while i<len(g):
            while j<len(s) and g[i]>s[j]:
                j += 1
            if j==len(s): break
            else:
                i += 1
                j += 1
                res += 1
        return res