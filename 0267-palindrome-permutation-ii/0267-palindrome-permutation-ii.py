class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)
        oddchar = ""
        for c in count.copy():
            if count[c] % 2 == 1:
                if oddchar == "":
                    oddchar = c
                else:
                    return []
            count[c] //= 2
            if count[c] == 0:
                count.pop(c)
        
        def constructBuffer(buffer,res):
            if not count:
                res.append("".join(buffer[:]+[oddchar]+buffer[::-1]))
                return
            for c in count.copy(): 
                count[c] -= 1
                if count[c] == 0:
                    count.pop(c)
                buffer.append(c)
                constructBuffer(buffer,res)
                count[c] = count.get(c,0) + 1
                buffer.pop()
        buffer = []
        res = []
        constructBuffer(buffer, res)
        return res