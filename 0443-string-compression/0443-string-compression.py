class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0 #i iterate thru original list j is the write index, j <= i always holds
        ct = 0
        for i in range(len(chars)):
            ct += 1
            if i == len(chars) - 1 or chars[i] != chars[i+1]: #time to wrap the current group
                chars[j] = chars[i]
                j += 1
                if ct > 1:
                    ctStr = str(ct)
                    for c in ctStr:
                        chars[j] = c
                        j += 1
                ct = 0
            
        return j