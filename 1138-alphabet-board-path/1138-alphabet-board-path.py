class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        buffer = []
        positions = [[(ord(ch)-ord("a"))//5, (ord(ch)-ord("a"))%5] for ch in target]
        r0,c0 = 0,0
        for r,c in positions:
            flag = False
            if r==5 and c==0:
                if r0==5:
                    buffer.append("!")
                    continue
                else:
                    flag = True
                    r,c = 4,0
            buffer.extend(["D"]*(r-r0) if r>=r0 else ["U"]*(r0-r))
            buffer.extend(["R"]*(c-c0) if c>=c0 else ["L"]*(c0-c))
            if flag:
                buffer.append("D")
                r,c = 5,0
            buffer.append("!")
            r0,c0 = r,c
        return "".join(buffer)