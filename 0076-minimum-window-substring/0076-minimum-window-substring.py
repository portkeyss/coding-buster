class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        A = Counter(t)
        B = Counter()
        l = 0
        i = 0
        res = ""
        for j in range(n):
            if s[j] in A:
                B[s[j]] += 1
                if B[s[j]]==A[s[j]]: l += 1
                if l==len(A):
                    while i<j:
                        if s[i] not in A:
                            i += 1
                        elif B[s[i]]>A[s[i]]:
                                B[s[i]] -= 1
                                i += 1
                        else:
                            break
                    if res=="" or len(res)>j+1-i: res = s[i:j+1]
        return res