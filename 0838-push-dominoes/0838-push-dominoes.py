class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        buffer = []
        for i in range(n):
            if dominoes[i]==".":
                continue
            elif dominoes[i]=="R":
                j = len(buffer)-1
                if buffer==[] or buffer[-1]=="L":
                    buffer += ["."]*(i-1-j)
                else:
                    buffer += ["R"]*(i-1-j)
                buffer.append("R")
            else: #dominoes[i]=="L"
                j = len(buffer)-1
                if buffer==[] or buffer[-1]=="L":
                    buffer += ["L"]*(i-1-j)
                else:#buffer and buffer[-1]=="R":
                    l = (i-1-j)
                    x = ["R"]*(l//2)+["."]+["L"]*(l//2) if l%2==1 else ["R"]*(l//2)+["L"]*(l//2)
                    buffer += x
                buffer.append("L")
        if len(buffer)<n:
            j = len(buffer)-1
            if buffer==[] or buffer[-1]=="L":
                buffer += ["."]*(n-1-j)
            else:
                buffer += ["R"]*(n-1-j)
        return "".join(buffer)