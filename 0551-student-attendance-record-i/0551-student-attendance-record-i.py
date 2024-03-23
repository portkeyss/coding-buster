class Solution:
    def checkRecord(self, s: str) -> bool:
        totA = 0
        consecL = 0
        for c in s:
            if c=="A":
                totA+=1
                if totA>=2: return False
            if c=="L":
                consecL += 1
                if consecL==3: return False
            else:
                consecL = 0
        return True