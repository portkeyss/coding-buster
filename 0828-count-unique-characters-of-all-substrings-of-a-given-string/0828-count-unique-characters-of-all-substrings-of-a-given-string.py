class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        charIdxList = defaultdict(list)
        for i, c in enumerate(s):
            charIdxList[c].append(i)
        
        def substrings(length):
            return length * (1 + length) //2
        
        ans = 0
        for l in charIdxList.values():
            for j in range(len(l)):
                cur = l[j]
                prev = l[j-1] if j>0 else -1
                nxt = l[j+1] if j<len(l)-1 else n
                ans += substrings(nxt-prev-1) - substrings(cur-prev-1) - substrings(nxt-cur-1)
        return ans % (10**9+7)