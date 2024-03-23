class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        s = set()
        for i in range(m):
            for j in range(m-i):
                s.add("#"*i+stamp[i:m-j]+"#"*j)
        ans = []
        init = "#"*n
        for i in range(n-m+1):
            if target[i:i+m] in s:
                target= target[:i]+"#"*m+target[i+m:]
                ans.append(i)
        if target==init: return ans[::-1]
        for i in range(n-m+1,-1,-1):
            if target[i:i+m] in s:
                target= target[:i]+"#"*m+target[i+m:]
                ans.append(i)
        if target==init: return ans[::-1]
        else: return []