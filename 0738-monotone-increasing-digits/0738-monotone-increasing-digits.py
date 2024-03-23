class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nlist = list(str(N))
        sz = len(nlist)
        i = 1
        j = 0
        while i < sz and nlist[i-1] <= nlist[i]:
            if nlist[i-1] < nlist[i]:
                j = i 
            i += 1
        if i == sz:
            return N
        nlist[j] = chr(ord(nlist[j])-1)
        for k in range(j+1,sz):
            nlist[k] = '9'
        return int(''.join(nlist))
            
            
        