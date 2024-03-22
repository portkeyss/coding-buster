class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        l = []
        r = []
        while i < j:
            if s[i] in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                l.append(s[j])
                r.append(s[i])
                i += 1
                j -= 1
            elif s[i] in "aeiouAEIOU" and s[j] not in "aeiouAEIOU":
                r.append(s[j])
                j -= 1
            elif s[i] not in "aeiouAEIOU" and s[j] in "aeiouAEIOU":
                l.append(s[i])
                i += 1
            else:
                l.append(s[i])
                r.append(s[j])
                i += 1
                j -= 1
        
        mid = [""]
        if i == j:
            mid = [s[i]] 
        r.reverse()
        return "".join(l + mid + r)