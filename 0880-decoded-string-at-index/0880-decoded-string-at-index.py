class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        n = len(s)
        i = 0
        length = 0
        stk = []
        while i < n:
            j = i
            while j<n and s[j].isalpha():
                j += 1
            ct = 1
            l = j
            while l<n and s[l].isnumeric():
                ct *= int(s[l])
                l+=1
            stk.append((length, s[i:j]))
            length = (length + len(s[i:j]))*ct
            if length < k:
                i = l
            else:
                break

        k -= 1
        while stk:
            curIdx,curStr = stk.pop()
            unitLength = curIdx+len(curStr)
            h = k%unitLength
            if h < curIdx:
                k = h
            else:
                return curStr[h-curIdx]