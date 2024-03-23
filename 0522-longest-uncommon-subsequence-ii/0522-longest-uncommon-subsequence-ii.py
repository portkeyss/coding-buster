class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        counter = Counter(strs)
        ss = list(counter.keys())
        ss.sort(key=lambda x:len(x), reverse=True)
        def isSubsequence(a,b):#check if b is a subsequence of a
            i, j = 0, 0
            m, n = len(a), len(b)
            while j<n:
                while i<m and a[i] != b[j]:
                    i += 1
                if i==m: return False
                i += 1
                j += 1
            return True
        for i,s in enumerate(ss):      
            if counter[s]==1 and not any(isSubsequence(ss[j],s) for j in range(i)):
                return len(s)
        return -1