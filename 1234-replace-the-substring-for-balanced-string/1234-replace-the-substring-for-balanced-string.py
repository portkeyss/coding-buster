class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        count = Counter(s)
        excess = {ch:ct-n//4 for ch,ct in count.items() if ct>n//4}
        m = len(excess)
        if m==0: return 0
        #find minimum window to contain excess chars
        window = Counter()
        res = n
        i = 0
        unfilled = True
        for j in range(n): 
            if s[j] in excess:
                window[s[j]]+=1
                if window[s[j]]==excess[s[j]]:
                    m -= 1
                    if m==0: unfilled = False
            if unfilled: continue
            while i<=j:
                if s[i] in excess:
                    if window[s[i]]==excess[s[i]]: break
                    else: window[s[i]] -= 1
                i += 1
            res = min(res, j-i+1)
            j += 1
        return res