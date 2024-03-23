class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        lower = upper = digit = False
        for c in s:
            if c.islower(): lower = True
            elif c.isupper(): upper = True
            elif c.isnumeric(): digit = True
        missing = 3-(lower + upper + digit)
        
        oned = twod = 0
        replace = add = 0
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                if (j-i)%3 == 0: oned += 1
                elif (j-i)%3 == 1: twod += 2
                replace += (j-i)//3
                add += (j-i-1)//2
            i = j
        
        if len(s) < 6:
            return max(6-len(s), missing, add)
        if len(s) <= 20:
            return max(missing, replace)
        
        delete = len(s)-20
        replace -= min(delete, oned)
        replace -= min(max(delete-oned, 0), twod)//2
        replace = max(replace-max(delete-oned-twod, 0)//3,0)

        return delete + max(missing, replace)